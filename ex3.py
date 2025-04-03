nome_produto = (input(" digite o nome do produto"))
quantidade= (input("digite a quantidade do produto"))
preco_uni= float(input("digite o preco unitario"))
valor=preco_uni*quantidade
desconto =valor - valor* 0.05

if valor<=100:
    print(f"total com desconto R${valor}")
else:
    print(f"Com desconto: {desconto}")