#!/usr/bin/env python3
"""Verify the repository without importing numerical code or writing output files.

Only the Python standard library is required. Checksums bind the distributed
extended supplement, simulation data, programs, and numerical inputs. A real root
.git directory is allowed in a local checkout but its contents are not audited.
"""
from __future__ import annotations
import ast
import hashlib
import json
from pathlib import Path
import re
import sys
sys.dont_write_bytecode = True


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def manifest(path: Path) -> dict[str, str]:
    entries = {}
    for line in path.read_text(encoding='utf-8').splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  ([^\r\n]+)', line)
        if not m:
            raise ValueError('Malformed checksum entry')
        h, name = m.groups()
        p = Path(name)
        if p.is_absolute() or '..' in p.parts or '\\' in name or name in entries or name == path.name:
            raise ValueError('Unsafe, duplicate, or circular checksum entry')
        entries[name] = h
    return entries


def inventory(root: Path, allow_git: bool = False) -> tuple[set[str], bool]:
    found, git_present = set(), False
    def visit(directory):
        nonlocal git_present
        for p in directory.iterdir():
            rel = p.relative_to(root).as_posix()
            if p.is_symlink():
                raise ValueError('Symbolic link: ' + rel)
            if allow_git and rel == '.git':
                if not p.is_dir():
                    raise ValueError('Root .git must be a real directory')
                git_present = True
                continue
            if p.is_file():
                if p.stat().st_nlink != 1:
                    raise ValueError('Hard-linked file: ' + rel)
                found.add(rel)
            elif p.is_dir():
                visit(p)
            else:
                raise ValueError('Nonregular entry: ' + rel)
    visit(root)
    return found, git_present


def verify(root: Path) -> dict:
    checks = []
    def check(name, condition, detail=None):
        checks.append({'check': name, 'passed': bool(condition), 'detail': detail})
        if not condition:
            raise ValueError(name)
    try:
        root = root.resolve(strict=True)
        expected = manifest(root/'SHA256SUMS.txt')
        actual, git = inventory(root, True)
        check('Exact repository file membership', actual == set(expected)|{'SHA256SUMS.txt'}, len(actual))
        check('Every repository checksum matches', all(digest(root/n) == h for n,h in expected.items()))
        sim = root/'simulation'
        nested = manifest(sim/'SHA256SUMS.txt')
        members, _ = inventory(sim)
        check('Exact numerical-subtree membership', members == set(nested)|{'SHA256SUMS.txt'}, len(members))
        check('Every numerical-subtree checksum matches', all(digest(sim/n) == h for n,h in nested.items()))
        pinned = json.loads((sim/'config/reference_inputs.json').read_text())['unchanged_source_data_sha256']
        check('All recorded scientific input bindings match', all(digest(sim/n) == h for n,h in pinned.items()), len(pinned))
        bindings = json.loads((sim/'config/companion_asset_map.json').read_text())['bindings']
        check('Computational section-to-asset bindings match', all(digest(sim/x['path']) == x['sha256'] for x in bindings), len(bindings))
        comparisons = json.loads((sim/'config/supersession.json').read_text())['supersessions']
        check('Original/reference precision bindings match', all(digest(sim/x[k]) == x[k+'_sha256'] for x in comparisons for k in ['old','new'] if k in x))
        check('Only the extended supplement in documents',
              {p.name for p in (root/'documents').iterdir()} == {'extended.pdf'}
              and (root/'documents/extended.pdf').is_file())
        check('Repository contains only declared functional directories',
              {p.name for p in root.iterdir() if p.is_dir() and p.name != '.git'}
              == {'documents','simulation','data','docs','tools'})
        csvs = list((root/'data/plotting').iterdir())
        check('Twelve publication plotting CSVs',len(csvs)==12 and all(p.suffix=='.csv' for p in csvs))
        for n in actual:
            if n.endswith('.py'):
                ast.parse((root/n).read_text(encoding='utf-8'),filename=n)
        check('All Python sources parse without imports',True)
        check('Numerical programs and launch interface present',len(list(sim.rglob('*.py')))==32 and (sim/'reproduce_all.sh').is_file())
        check('Descriptive plotting interfaces present',all((root/'tools'/n).is_file() for n in ['export_deterministic_plot_data.py','export_accuracy_plot_data.py']))
        allowed_pdfs={'documents/extended.pdf','simulation/docs/COMPUTATIONAL_COMPANION.pdf'}
        check('Only declared document PDFs; no nested archives', {n for n in actual if n.endswith('.pdf')}==allowed_pdfs and not any(n.endswith('.zip') for n in actual))
        forbidden_suffix={'.pyc','.pyo','.ttf','.otf','.woff','.woff2','.pfb','.pfa','.afm','.tfm','.vf','.log','.synctex','.aux','.out','.toc','.fls','.fdb_latexmk'}
        check('No loose fonts caches or build logs',not any(Path(n).suffix.lower() in forbidden_suffix or '__pycache__' in Path(n).parts or '.DS_Store' in n for n in actual))
        check('Byte-preserving Git attributes','* -text' in (root/'.gitattributes').read_text())
        check('No new license declaration',json.loads((sim/'config/package_info.json').read_text())['license_selected'] is False and not any(Path(n).name.upper().startswith(('LICENSE','COPYING'))for n in actual))
        return {'status':'PASS','checks_passed':len(checks),'checks_total':len(checks),'files':len(actual),'numerical_files':len(members),'scientific_routes_executed':False,'root_git_metadata_not_audited':git,'checks':checks}
    except (OSError,ValueError,KeyError,SyntaxError) as exc:
        return {'status':'FAIL','checks_passed':sum(c['passed']for c in checks),'checks_total':len(checks),'error':str(exc),'checks':checks}


if __name__ == '__main__':
    if len(sys.argv)>2:
        raise SystemExit('Usage: python3 -B verify_repository.py [repository_root]')
    result=verify(Path(sys.argv[1]) if len(sys.argv)==2 else Path(__file__).resolve().parent)
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if result['status']=='PASS' else 1)
