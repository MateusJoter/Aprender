texto_1 = "O sol brilha forte no céu azul"

texto_2 = "O céu azul anuncia um dia de sol intenso"

conj_1 = set(texto_1.lower().split())
conj_2 = set(texto_2.lower().split())

print(f"Palavras em comum: {conj_1.intersection(conj_2)}")