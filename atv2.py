print("Sabendo que y = ax² + bx + c:")


a = int(input("Digite a: \n"))
b = int(input("Digite b: \n"))
c = int(input("Digite c: \n"))


x = int(input("Digite um valor para x: \n"))


res1 = a*x*x + b*x + c


if res1 > 0:
    final = res1**(1/2)
    print("Resultado da raiz de y: ", final)
else:
    print("Resultado da função é y =",res1,". Sua raiz quadrada não pertence aos Reais.")
