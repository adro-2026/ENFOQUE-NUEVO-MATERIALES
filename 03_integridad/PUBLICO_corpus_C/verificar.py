#!/usr/bin/env python3
"""
Verificador público del compromiso. No necesita la clave privada ni el contenido.

  1) Recalcular la raíz desde el manifiesto:
       python3 verificar.py manifiesto MANIFIESTO_A.csv.gz RAIZ_A.txt
  2) Verificar un mensaje revelado por el autor:
       python3 verificar.py prueba PRUEBA_convX_nodoY.json RAIZ_A.txt
"""
import csv, gzip, hashlib, json, sys
from collections import OrderedDict

sha = lambda b: hashlib.sha256(b).digest()
interno = lambda a, b: sha(b"\x01" + a + b)
canon = lambda o: json.dumps(o, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")

def raiz(hs):
    while len(hs) > 1:
        hs = [interno(hs[i], hs[i + 1]) if i + 1 < len(hs) else hs[i] for i in range(0, len(hs), 2)]
    return hs[0]

def aplicar(h, pasos):
    for lado, x in pasos:
        x = bytes.fromhex(x)
        h = interno(x, h) if lado == "izq" else interno(h, x)
    return h

def leer_raiz(p):
    return open(p).read().strip().lower()

if sys.argv[1] == "manifiesto":
    convs = OrderedDict(); declaradas = {}
    with gzip.open(sys.argv[2], "rt", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            c = int(r["conv_n"])
            convs.setdefault(c, []).append(bytes.fromhex(r["hoja_sha256"]))
            if r["raiz_conv_sha256"]:
                declaradas[c] = r["raiz_conv_sha256"]
    raices = []
    for c, hs in convs.items():
        rc = raiz(hs)
        if rc.hex() != declaradas.get(c):
            sys.exit(f"ERROR: la raíz de la conversación {c} no coincide")
        raices.append(rc)
    calc = raiz(raices).hex()
    ok = calc == leer_raiz(sys.argv[3])
    print(f"conversaciones: {len(convs)}  hojas: {sum(map(len, convs.values()))}")
    print(f"raíz calculada: {calc}")
    print("COINCIDE con la raíz publicada" if ok else "NO COINCIDE")
elif sys.argv[1] == "prueba":
    p = json.load(open(sys.argv[2], encoding="utf-8"))
    h = sha(b"\x00" + bytes.fromhex(p["sal_hex"]) + canon(p["contenido"]))
    h = aplicar(aplicar(h, p["camino_en_conv"]), p["camino_en_corpus"])
    print("VÁLIDA: ese contenido estaba en el corpus comprometido" if h.hex() == leer_raiz(sys.argv[3]) else "NO VÁLIDA")
