print("Calculadora de Reajuste Salarial")
print("~"*30)

print("Porcentagens re deajuste:\n1 - 3,43%\n2 - 2,07%\n3 - 6,58%")
rej = int(input("Escolha o reajuste que você deseja: "))
print("~"*30)
sal = int(input("Digite o valor de seu salário: "))
print("~"*30)

if rej == 1:
    print("Reajuste escolhido 1.")
    print("Salário reajustado: ", sal * 343/10000 + sal)
elif rej == 2:
    print("Reajuste escolhido 2.")
    print("Salário reajustado: ", sal * 207/10000 + sal)
elif rej == 3:
    print("Reajuste escolhido 3.")
    print("Salário reajustado: ", sal * 658/10000 + sal)
else:
    print("Você é burro ou quer um real?")
