senha_correta = "python123"
tenativa = 0 

while tenativa < 3:
    senha = input("Digite sua senha: ")
    if senha == senha_correta:
        print("Acesso liberado!")
        break
    else:
        print("Senha incorreta")
    tenativa += 1 
else:
    print("Limete de tentativas atigindidas")