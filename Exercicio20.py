nota = float(input(" Digite a sua nota de 0 a 10"))

if nota < 0 or nota > 10: 
    print("Nota inválida")
elif nota >=7:
    print("Aprovado")
elif nota >5: 
    print("Recuperação")
else: 
    print("Reprovado")