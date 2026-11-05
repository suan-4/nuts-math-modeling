"""Validate release links, UTF-8, frontmatter basics and Python syntax."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "nuts-math-modeling"
errors = []
for path in ROOT.rglob('*'):
    if not path.is_file() or '.git' in path.parts or '__pycache__' in path.parts:
        continue
    if path.suffix not in {'.md', '.py', '.yml', '.yaml'}:
        continue
    try:
        content = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        errors.append(f'Not UTF-8: {path.relative_to(ROOT)}')
        continue
    if path.suffix == '.py':
        try:
            compile(content, str(path.relative_to(ROOT)), 'exec')
        except SyntaxError as error:
            errors.append(f'Syntax error: {path.relative_to(ROOT)}:{error.lineno}')
    if path.suffix == '.md':
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in target or target.startswith('#'):
                continue
            if not (path.parent / target.split('#', 1)[0]).exists():
                errors.append(f'Broken link: {path.relative_to(ROOT)} -> {target}')
text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
if not text.startswith('---\n') or 'name: nuts-math-modeling\n' not in text:
    errors.append('Invalid skill frontmatter')
if re.search(r'C:[\\/]+Users[\\/]+[^\s/\\]+[\\/]+Desktop', text):
    errors.append('Personal desktop path in skill entrypoint')
if errors:
    raise SystemExit('\n'.join(errors))
print('Release validated: UTF-8, local links, Python syntax and skill entrypoint.')
