def calc(H, M):
    if M < 45:
        M = 60 - (45 - M)
        switch = True
        
    if H == 0 and switch == True:
        return 23, M
    elif H != 0 and switch == True:
        return H-1, M
    return H, M

x = input()
x1, x2 = x.split(' ')
H1, M1 = int(x1), int(x2)

H2, M2 = calc(H1, M1)
print(str(H2), str(M2))

