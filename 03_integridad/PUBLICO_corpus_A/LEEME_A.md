# Compromiso criptográfico — Corpus A

Este paquete demuestra que el corpus A existe y no fue alterado, sin mostrar su contenido.

Raíz del corpus A (SHA-256): ver RAIZ_A.txt
Conversaciones: 3265 · Nodos: 157725 · Rango: 2024-06-28 a 2026-10-22 (UTC)

Qué contiene:
- MANIFIESTO_A.csv.gz: una fila por nodo con número de conversación, número de nodo, rol, fecha, tipo de contenido y hash. Sin texto, sin títulos, sin IDs.
- RAIZ_A.json: conteos, hashes de los archivos originales y esquema del árbol.
- verificar.py: cualquiera puede recalcular la raíz desde el manifiesto (Python 3, sin dependencias).

Cada hash lleva una sal secreta, así que no se puede adivinar el contenido ni de un mensaje corto. El autor puede revelar un mensaje puntual con su prueba de inclusión, y verificar.py comprueba que estaba en el corpus desde el principio.

Verificar:
    python3 verificar.py manifiesto MANIFIESTO_A.csv.gz RAIZ_A.txt
    python3 verificar.py prueba PRUEBA_convX_nodoY.json RAIZ_A.txt
