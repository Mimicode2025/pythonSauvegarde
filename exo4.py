while True:
    nombre = int(input("veullez resaisir le nombre :"))
    if nombre > 0:
        break
fois = 0
while nombre % 2 == 0 and nombre != 0:
    nombre = nombre // 2
    fois += 1
print(f"le nombre est {fois} fois divisible par 2")
