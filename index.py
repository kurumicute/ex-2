ls = ['the lord of the rings','anaconda','legally blonde','gone with the wind']
s = input()
if s == '1':
    print([x **3 for x in range(10)])
elif s == '2':
    print([x**3 for x in range(10) if x %2 == 0])
elif s == '3':
    print([(x,x ** 3)] for x in range(10) if x % 2 == 1)
elif s == '4':
    print([s.capitalize()] for s in ls)
else:
    print("END")