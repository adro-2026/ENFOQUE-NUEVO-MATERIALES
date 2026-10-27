# Compromiso criptográfico — Corpus B

Este paquete demuestra que el corpus B existe y no fue alterado, sin mostrar su contenido.

Raíz del corpus B (SHA-256): ver RAIZ_B.txt
Conversaciones: 296 · Nodos: 7928 · Rango: 2025-08-07 a 2026-10-19 (UTC)

Qué contiene:
- MANIFIESTO_B.csv.gz: una fila por nodo con número de conversación, número de nodo, rol, fecha, tipo de contenido y hash. Sin texto, sin títulos, sin IDs.
- RAIZ_B.json: conteos, hashes de los archivos originales y esquema del árbol.
- verificar.py: cualquiera puede recalcular la raíz desde el manifiesto (Python 3, sin dependencias).

Cada hash lleva una sal secreta, así que no se puede adivinar el contenido ni de un mensaje corto. El autor puede revelar un mensaje puntual con su prueba de inclusión, y verificar.py comprueba que estaba en el corpus desde el principio.

Verificar:
    python3 verificar.py manifiesto MANIFIESTO_B.csv.gz RAIZ_B.txt
    python3 verificar.py prueba PRUEBA_convX_nodoY.json RAIZ_B.txt
