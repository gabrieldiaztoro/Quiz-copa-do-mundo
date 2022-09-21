print ("Bem vindo ao quiz Copa do Mundo")
resposta_comeco = input("Vamos comecar? (S/N): \n")

if resposta_comeco != "S":
    quit()

score = 0    
    
print ("Ok, Bora la! \n")   
print ("Pergunta numero 1. \n Quem e o atual campeao da Copa do Mundo? (2018) \n (A) Alemanha \n (B) Franca \n (C) Espanha \n")
resposta_1 = input ("Resposta: ")

if resposta_1 == "B":
    print ("Acertou!! \n")
    score = score + 1
else: 
    print ("errrou!! \n")

print ("Pergunta numero 2. \n Quantas vezes o Brasil ganhou a Copa do Mundo? \n (A) 5 vezes \n (B) 6 vezes \n (C) 4 vezes \n")
resposta_2 = input ("Resposta: ")

if resposta_2 == "A":
    print ("Acertou!! \n")
    score = score + 1
else: 
    print ("errrou!! \n")    

print ("Pergunta numero 3. \n Quantas vezes o Inglaterra ganhou a Copa do Mundo? \n (A) 1 vezes \n (B) 2 vezes \n (C) 3 vezes \n")
resposta_3 = input ("Resposta: ")

if resposta_3 == "A":
    print ("Acertou!! \n")
    score = score + 1
else: 
    print ("errrou!! \n")    

print (f"TABELA DE PONTUACAO: \n Pessimo:0 \n Ruim:1 \n Sabe um pouco:3 \n \n sua pontuacao e {score} \n")

print ("Fim do quiz!")

