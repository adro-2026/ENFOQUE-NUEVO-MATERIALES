# 03 — Traza y disponibilidad
Versión 1.0 · 27/10/2026. Alcance: encargo 03.

## Lectura y comprobaciones efectivas
- Prompt íntegro: 1xEwy6sG_qWqddZ-x3j2zl5XNd9FDQnXb.
- Base MD 1.2 recuperada íntegra en contenido; lectura focal completa del capítulo 10, H y S26–S28. No se declara lectura integral del resto ni inspección del PDF equivalente.
- Nueve anotadores A01–A09 recuperados y leídos completos. IDs y contenido conservados en las fuentes originales. A01 1B5jEmfgI0bxD4yancE5oKitkACK-eKDo; A02 1eAx4z85F-UmT36vzeSogy_QypbgT6v9t; A03 1rrcW9geMkXcZLH40HM3oGpDHahP7JGEd; A04 1US4LCRV2EDfNIvjJoB4gR_OhrxqcjFJ8; A05 1G5tvC2MLx4_HoPXevCMIk4gKz1co9N2X; A06 1Vh3TfQwkxTwd-no5Y0kbK_R5uVVKw7eY; A07 1qN8VawisogR9iyK19o85CaNPNHTTwuoZ; A08 1LXf0ZvPPd4nPfaylVIPtXpiObWz4P5G8; A09 1u21S3VfLmJ-PbigD_goXvBqCv4lR0s0b.
- Texto recuperado íntegro del informe principal A06: 11eELSsiQnRmYLxKAzPyDOHgLUUPunENs, incluidas tablas de ciclos y frames. La lectura es textual, no inspección de imágenes incrustadas.
- Listadas carpetas S27 y sus subcarpetas 01-Informes y 02-Evidencia. El listado devolvió anotadores/DOCX y cuatro PDF; no devolvió originales MP4 ni los documentos principales A01/A05. Búsquedas Informe_prediccion y Screenrecorder-2026-09-30 solo localizaron el anotador A05 como fuente pertinente.
- Metadatos actuales y listas de revisiones de ambos destinos S28 consultados. IDs exactos iguales a los de la base. MD actual 259705 bytes; PDF 4506278 bytes; títulos actuales v0_22. Se comprobaron metadatos de revisión, no bytes/contenido histórico.
- Carpeta destino listada antes de escribir: contenía cuatro prompts y dos bases; ninguna salida previa 03. Se crean salidas 03 versión 1.0, sin reemplazar fuentes ni archivos de otros encargos.

## Acceso fallido y evidencia mediada
| Fuente | Intento y resultado | Consecuencia |
|---|---|---|
| S26 Informes.zip, 1_GWVj2mh9CpuQEqU2pvDl04Q-9r7Iego | Metadatos correctos: ZIP 16775759 bytes. Dos fetch raw y un fetch legible devolvieron Transport closed | No se abrieron ANOMALIA_PERSISTENCIA.docx ni carátula en esta ejecución; sus datos se atribuyen a base 1.2 |
| S20 consolidado, 1kKXmVmvJjxz2Xa8WuGgSIeZ4pm-cCUCf | Metadatos correctos: ZIP 47058083 bytes. Fetch raw devolvió Transport closed | No hay nuevo cotejo JSON; se distingue del cotejo previo comunicado en H |
| Captura 1000505232.jpg | Búsqueda por nombre devolvió referencias textuales; búsqueda restringida a imágenes devolvió cero resultados | No hay nueva inspección de píxeles; descripción atribuida a H/S28 |
| Original A05 | Búsqueda por nombre del recording y nombre del informe no localizó original accesible | Cronología procede del anotador, sin tiempos frame nuevos |
| Originales marzo/A01/A06 | No se materializaron ni inspeccionaron MP4/capturas | No se declara auditoría audiovisual actual |

Los errores iniciales de argumentos de metadatos/listado se corrigieron y las operaciones terminaron correctamente; no equivalen a denegación de acceso a los archivos. Los fallos Transport closed sí impidieron obtener los ZIP.

## Aporte comprobado de esta ejecución
Las revisiones nombradas v0_12 tienen exactamente los tamaños que H atribuye a v0.13: MD 221218 y PDF 4441174 bytes. Fueron guardadas 26/10 a 22:56:25/30 ART. Las nombradas v0_13 fueron guardadas a 23:24:27/33 ART con 233287/4458651 bytes. No se cambió la base: se propone corregir la asociación en la próxima integración. Los revisionId se conservan en la matriz.

## Pendientes concretos
1. Recuperar S26 y S20 para releer informe/carátula y reproducir índice inverso parent. La conclusión actual de marzo tiene respaldo mediado, no replicación actual.
2. Incorporar originales A05 y A01 e informes principales/frames para fijar los eventos visuales exactos y el contenido de coordenadas. No inventar frame números.
3. Recuperar la captura o el registro contemporáneo S28 para emparejar el aviso con los guardados de 22:56/23:24 ART. Es la única aclaración que podría requerir Adro; el método ya es integrable.
4. Si se obtienen revisiones históricas, verificar versión interna y hash: originalFilename y tamaño son metadatos, no identidad semántica suficiente.
5. No se modifican HOLDOUT, comparaciones A/B/C ni resultados favorables a C. A08 registra su propio contraste preliminar; no se usa aquí para establecer mecanismos.

## Fuentes enlazadas
- [Base 1.2](https://drive.google.com/file/d/1xHRsVPaaCmEy0mWKo5pt8cMegyi7KbrU/view)
- [Informes.zip S26](https://drive.google.com/file/d/1_GWVj2mh9CpuQEqU2pvDl04Q-9r7Iego/view)
- [Consolidado S20](https://drive.google.com/file/d/1kKXmVmvJjxz2Xa8WuGgSIeZ4pm-cCUCf/view)
- [Serie S27](https://drive.google.com/drive/folders/1XsSi-wVrFf83y6BLVnVoZ2XHhNfRjaKA)
- [MD histórico S28](https://drive.google.com/file/d/1V2JhI3qPT6cu-tgdXPvvzpo_BLKqRNMk/view)
- [PDF histórico S28](https://drive.google.com/file/d/19pjBBOiSRzGsWZTBm6AJofykYG23dZRb/view)


