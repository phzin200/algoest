# #taboada do 7 
# print("tabuada do 7:") 
# for i in range (1,11): 
#     print ("7 x", i, "=", 7 * i) 
    


# #taboada do 8
# print("tabuada do 8:") 
# for i in range (1,11): 
#     print ("8 x", i, "=", 8 * i)
    
    
    
# #taboada do 9
# print("tabuada do 9:") 
# for i in range (1,11): 
#     print ("9 x", i, "=", 9 * i)


#UTILIZANDO FUNCAO:
#

def tabuada (numero): 
    print(f"tabuada do {numero}:")
    for i in range (1,11): 
        print (f"{numero} x {i} = {numero * i}") 
        
#exibindo tabuada 
tabuada(7)
tabuada(8) 
tabuada(9) 


# 
# utilizando lista e contador para exibir tabuada
# 
# def tabuada (numero):                                 
#    print(f"tabuada do {numero}:") 
#    for i in range (1,11): 
#          print (f"{numero} x {i} = {numero * i}") 

# for i in range (1,101): 
#     tabuada(i)



#tabuada personalizada 
# def tabuada_personalizada(base, inicio, fim): 
#     print (f"tabuada do {base} de {inicio} a {fim}:") 
#     for j in range (inicio, fim + 1 ): 
#         print (f"{base} x {j} = {base * j}") 
        
# #uso
# tabuada_personalizada ( 7 , 1 , 10)  # tabuada do 7 de 1 a 10 
# tabuada_personalizada ( 5, 5, 15 ) # tabuada do 5 de 5 a 15 