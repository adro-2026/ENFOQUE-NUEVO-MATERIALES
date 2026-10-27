# ENFOQUE NUEVO — materiales documentales del informe

Repositorio de respaldo documental del proyecto **ENFOQUE NUEVO**. La versión alojada en `00_informe/` es un **estado de trabajo** del manuscrito, no el PDF final. La revisión editorial y construcción del PDF definitivo se desarrollan fuera de este repositorio.

## Estructura

- [00_informe](00_informe/): manuscrito MD y PDF provisional de lectura (v0.22).
- [01_tests](01_tests/): 39 fichas de pruebas de la serie T, con la numeración original y sus huecos conservados.
- [02_informes](02_informes/): 18 documentos de apoyo, trazas e informes.
- [03_integridad](03_integridad/): compromisos criptográficos de los corpus A, B, C, raíces, verificadores y comprobante OpenTimestamps.
- [04_visual](04_visual/): imagen documental incluida en el recorrido.
- [FUENTES_REFERENCIADAS.json](FUENTES_REFERENCIADAS.json): referencias documentales; identifica también fuentes que permanecen en su ubicación de origen.
- [INVENTARIO.md](INVENTARIO.md): inventario actualizado de **este repositorio**, con rutas, tamaños y hashes SHA-1 de los blobs Git.
- [INVENTARIO.json](INVENTARIO.json): inventario SHA-256 del **paquete ZIP de preparación**, conservado como fuente original. No debe utilizarse como inventario idéntico de las versiones actuales del manuscrito.

## Versiones documentales

El traslado partió de `ENFOQUE_NUEVO_MATERIALES_PREPARADOS.zip` (83 archivos). Se incorporaron sus materiales faltantes respetando sus bytes y la estructura original. Ya existían dos versiones de trabajo diferentes que **no se sobrescribieron**:

| Ruta | Tamaño en ZIP de preparación | Tamaño actual en GitHub |
|---|---:|---:|
| `00_informe/INFORME.md` | 259705 | 259722 |
| `00_informe/INFORME.pdf` | 4506278 | 5271755 |

Esta diferencia es de versiones provisionales, no de un PDF final publicado. Los archivos del ZIP de origen siguen disponibles en Drive.

## Verificación criptográfica

Los manifiestos contienen hashes y metadatos, no el texto íntegro de los diálogos. Los exports originales, las conversaciones completas y las claves privadas no se incluyeron en el traslado.

En cada subcarpeta `03_integridad/PUBLICO_corpus_X/`:

```bash
python3 verificar.py manifiesto MANIFIESTO_X.csv.gz RAIZ_X.txt
```

Sustituir `X` por `A`, `B` o `C`. Para comprobar la raíz global:

```bash
cd 03_integridad/RAIZ_GLOBAL_ABC
python3 verificar_global.py
```

Los verificadores locales de A, B, C y global se ejecutaron correctamente contra el paquete de preparación el 27-10-2026. Esto comprueba coherencia de las raíces; **no constituye verificación externa independiente del sello OpenTimestamps**.

**Estado:** repositorio privado. No cambiar su visibilidad ni publicar materiales adicionales sin revisión.
