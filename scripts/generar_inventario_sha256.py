#!/usr/bin/env python3
"""Genera SHA-256 de los archivos versionados, excluyendo el propio inventario."""
from pathlib import Path
import hashlib
import subprocess

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"INVENTARIO.md", "INVENTARIO_ACTUAL_SHA256.tsv"}

raw = subprocess.check_output(["git", "-C", str(ROOT), "ls-files", "-z"])
paths = sorted(p.decode("utf-8", errors="surrogateescape") for p in raw.split(b"\0") if p)
lines = ["ruta\tbytes\tsha256"]
for rel in paths:
    if rel in EXCLUDED:
        continue
    file = ROOT / rel
    if not file.is_file():
        continue
    sha = hashlib.sha256()
    with file.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            sha.update(chunk)
    lines.append(f"{rel}\t{file.stat().st_size}\t{sha.hexdigest()}")
(ROOT / "INVENTARIO_ACTUAL_SHA256.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Inventario: {len(lines) - 1} archivos con SHA-256")
