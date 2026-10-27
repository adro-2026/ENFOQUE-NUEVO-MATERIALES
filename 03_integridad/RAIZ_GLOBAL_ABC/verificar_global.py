import hashlib, json
d = json.load(open("RAIZ_GLOBAL.json")); r = d["raices"]
i = lambda a, b: hashlib.sha256(b"\x01" + a + b).digest()
g = i(i(bytes.fromhex(r["A"]), bytes.fromhex(r["B"])), bytes.fromhex(r["C"])).hex()
print("COINCIDE" if g == d["raiz_global_sha256"] == open("RAIZ_GLOBAL.txt").read().strip() else "NO COINCIDE")
