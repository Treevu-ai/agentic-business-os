#!/usr/bin/env python3
"""Genera un inventario básico de PDFs en el repositorio.

No depende de librerías externas: usa inspección binaria simple para extraer
metadatos mínimos (tamaño, hash SHA-256, páginas aproximadas por objetos /Page,
y título del diccionario Info cuando existe).
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class PdfInfo:
    name: str
    size_bytes: int
    sha256: str
    page_count: int | None
    title: str | None


def _extract_literal(metadata: bytes, key: bytes) -> str | None:
    # Busca patrones tipo /Title (texto)
    m = re.search(rb"/" + key + rb"\s*\((.*?)\)", metadata, re.S)
    if not m:
        return None
    raw = m.group(1)
    raw = raw.replace(rb"\(", b"(").replace(rb"\)", b")")
    return raw.decode("latin-1", errors="ignore").strip() or None


def inspect_pdf(path: Path) -> PdfInfo:
    data = path.read_bytes()

    sha256 = hashlib.sha256(data).hexdigest()
    size = len(data)

    # Conteo aproximado de páginas: /Type /Page excluyendo /Pages
    page_matches = re.findall(rb"/Type\s*/Page(?!s)\b", data)
    page_count = len(page_matches) if page_matches else None

    title = _extract_literal(data[:200_000], b"Title")

    return PdfInfo(
        name=path.name,
        size_bytes=size,
        sha256=sha256,
        page_count=page_count,
        title=title,
    )


def _human_size(n: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    size = float(n)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{n} B"


def build_report(items: list[PdfInfo]) -> str:
    lines: list[str] = []
    lines.append("# Inventario de PDFs del repositorio")
    lines.append("")
    lines.append(f"Total de archivos PDF: **{len(items)}**")
    lines.append("")
    lines.append("| Archivo | Tamaño | Páginas (aprox) | Título metadata | SHA-256 (primeros 12) |")
    lines.append("|---|---:|---:|---|---|")

    for i in sorted(items, key=lambda x: x.name.lower()):
        lines.append(
            "| "
            f"`{i.name}` | {_human_size(i.size_bytes)} | {i.page_count or 'N/D'} | "
            f"{(i.title or 'N/D').replace('|', '/')} | `{i.sha256[:12]}` |"
        )

    # Detectar duplicados por hash
    by_hash: dict[str, list[str]] = {}
    for i in items:
        by_hash.setdefault(i.sha256, []).append(i.name)

    duplicates = [group for group in by_hash.values() if len(group) > 1]
    lines.append("")
    lines.append("## Duplicados exactos (mismo SHA-256)")
    if duplicates:
        for group in duplicates:
            lines.append(f"- {', '.join(f'`{g}`' for g in sorted(group))}")
    else:
        lines.append("- No se detectaron duplicados exactos.")

    lines.append("")
    lines.append("## Nota")
    lines.append("- Este inventario no extrae texto interno; solo metadata binaria básica.")

    return "\n".join(lines) + "\n"


def main() -> int:
    root = Path.cwd()
    pdfs = sorted(root.glob("*.pdf"))
    infos = [inspect_pdf(p) for p in pdfs]

    report = build_report(infos)
    out = root / "INVENTARIO_REPO.md"
    out.write_text(report, encoding="utf-8")
    print(f"Inventario generado en: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
