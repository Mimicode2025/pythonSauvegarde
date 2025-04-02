def sont_amis(n, m):
    s1 = 0
    s2 = 0
    for i in range(2, n):
        if n % i == 0:
            s1 += i
    for j in range(2, m):
        if m % j == 0:
            s2 += j
    if s1 == m and s2 == n:
        return True


x = int(input("veullez saisir le premier nombre : "))
y = int(input("veullez saisir le second nombre : "))
if sont_amis(x, y):
    print(f"les nombre {x} et {y} sont amis")
