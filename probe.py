"""Probe: try to rename the contents dir and base_library.zip while the app runs."""
from __future__ import annotations

import pathlib

BASE = pathlib.Path('dist/toy')
RUNTIME = BASE / '.runtime'
lines: list[str] = []

for label, target in (
    ('.runtime (contents dir)', RUNTIME),
    ('.runtime/base_library.zip', RUNTIME / 'base_library.zip'),
):
    tmp = target.parent / (target.name + '_probe')
    try:
        target.rename(tmp)
        tmp.rename(target)
        lines.append(f'{label}: renameable')
    except OSError as e:
        lines.append(f'{label}: FAIL -> {e}')

report = '\n'.join(lines)
pathlib.Path('probe_result.txt').write_text(report, encoding='utf-8')
print(report, flush=True)
