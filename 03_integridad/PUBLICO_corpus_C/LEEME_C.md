# Compromiso criptográfico — Corpus C

Este paquete demuestra que el corpus C existe y no fue alterado, sin mostrar su contenido.

Raíz del corpus C (SHA-256): ver RAIZ_C.txt
Conversaciones: 457 · Mensajes: 27057 · Rango: 2026-01-03 a 2026-10-20 (UTC)
Tres conversaciones llegan sin mensajes desde el propio export de Claude; quedan comprometidas con sus metadatos tal como vinieron.

Qué contiene:
- MANIFIESTO_C.csv.gz: una fila por nodo con número de conversación, número de nodo, rol, fecha, tipo de contenido y hash. Sin texto, sin títulos, sin IDs.
- RAIZ_C.json: conteos, hashes de los archivos originales y esquema del árbol.
- verificar.py: cualquiera puede recalcular la raíz desde el manifiesto (Python 3, sin dependencias).

Cada hash lleva una sal secreta, así que no se puede adivinar el contenido ni de un mensaje corto. El autor puede revelar un mensaje puntual con su prueba de inclusión, y verificar.py comprueba que estaba en el corpus desde el principio.

Verificar:
    python3 verificar.py manifiesto MANIFIESTO_C.csv.gz RAIZ_C.txt
    python3 verificar.py prueba PRUEBA_convX_nodoY.json RAIZ_C.txt
