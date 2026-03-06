a = float(input("Digite o valor de 'A': "))
b = float(input("Digite o valor de 'B': "))
c = float(input("Digite o valor de 'C': "))

delta = b*2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    print("A equação possui uma raiz real.")
    x = (-b + delta**0.5) / (2*a)
    print(f"A raiz real é: {x}")
else:
    print("A equação possui duas raízes reais.")
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print(f"As raízes reais são: {x1} e {x2}")
