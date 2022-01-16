def flip(n):
    s = bin(n)[2:]
    t = s.maketrans("01","10")
    s = s.translate(t)
    s = (32-len(s))*"1"+s 
    return int(s,2)
for _ in range(int(input())):
    print(flip(int(input())))