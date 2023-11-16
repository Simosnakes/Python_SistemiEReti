num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))

somma_quad = num1**2 + num2**2
quad_somma = (num1 + num2)**2
diff_quad = num1**2 - num2**2
quad_diff = (num1 - num2)**2
risultati = [somma_quad, quad_somma, diff_quad, quad_diff]
print(risultati)