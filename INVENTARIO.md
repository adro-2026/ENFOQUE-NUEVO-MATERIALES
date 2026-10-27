# Inventario del repositorio — edición 1.4

El inventario actual reproducible está en **[INVENTARIO_ACTUAL_SHA256.tsv](INVENTARIO_ACTUAL_SHA256.tsv)**. Cada registro contiene la ruta relativa, el tamaño en bytes y el SHA-256 del archivo exacto del árbol final.

Regeneración desde una copia Git local con Python 3:

```bash
python3 scripts/generar_inventario_sha256.py
```

El script usa `git ls-files` para fijar el conjunto de rutas. Se excluyen solamente **`INVENTARIO.md`** y **`INVENTARIO_ACTUAL_SHA256.tsv`**, que contienen o describen el propio inventario, evitando autorreferencia. Los archivos no existentes en el árbol de trabajo no se incluyen.

**Nota histórica:** `INVENTARIO.json` conserva las huellas SHA-256 del **ZIP original de preparación** del repositorio. Es anterior al preprint 1.4 y no debe confundirse con el inventario actual.

El preprint 1.4 reemplaza las versiones provisionales de `00_informe/INFORME.md` y `00_informe/INFORME.pdf`; sus versiones anteriores quedan preservadas en Git. Los archivos de tests, informes anteriores, integridad y recursos originales se mantienen sin modificaciones. La inclusión del comprobante `.ots` no prueba por sí sola la validación externa del sello.
