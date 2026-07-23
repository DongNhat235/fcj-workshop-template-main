import re
from pathlib import Path

root = Path(__file__).resolve().parents[1] / 'content' / '5-Workshop'
pattern = re.compile(r'!\[([^\]]*)\]\(/images/5-Workshop/([^\)]+)\)')

for p in root.rglob('*.md'):
    text = p.read_text(encoding='utf-8')
    new_text, n = pattern.subn(r'{{< img "images/5-Workshop/\2" "\1" >}}', text)
    if n:
        p.write_text(new_text, encoding='utf-8')
        print(f'Updated {p.relative_to(root.parent)}: {n} replacements')
    else:
        print(f'No changes in {p.relative_to(root.parent)}')
