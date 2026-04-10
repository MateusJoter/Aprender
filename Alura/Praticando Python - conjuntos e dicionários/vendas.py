vendas = { 

    "Eletrônicos": [ 

        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 

        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 

    ], 

    "Eletrodomésticos": [ 

        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 

        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 

    ], 

    "Livros": [ 

        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 

        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 

    ] 

}

print("Total de vendas por categoria: \n")

for categoria in vendas:
    valor_vendido = 0
    for produto in vendas[categoria]:
        valor_vendido += produto['quantidade'] * produto['valor_unitario']
    print(f"- {categoria}: R$ {valor_vendido:.2f}\n")