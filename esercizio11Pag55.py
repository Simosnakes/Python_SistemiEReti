x = [0, 1, 2, 3, 5, 6, 7, 8]
y = []
z = []

lung = len(x)
mezzo = lung // 2

y.append(x[:mezzo])

y.append(5)

print(y)

z.append(x[mezzo:])

print(z)
