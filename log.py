print("\033[31m{}".format('Внимание за то что ответы правильные не отвечаю, нужно много тестов'))
print('введите уравнение в виде 2 4 * 3 9, первое число основание log, второе значение, следом знак действия, длинна примера неограничена,может считать 1 log, только целые числа')
s = input().split()
f=[]

def log(a, b):
    a=int(a)
    b=int(b)
    c = 1
    d = 1
    while a != d:
        d = b
        c = c + 1
        d = d ** c
        if d > a:
            if a>b:
                c=c-1
            else:
                c=c-2
            c = float(c)
            for g in range(1, 17):
                h = 10 ** g
                for i in range(10):
                    c = c + 1 / h
                    d = b
                    d = d ** c
                    if d > a:
                        c = c - 1 / h
                        continue
            break
    return (c)


for i in range(1, len(s) + 1, 3):
    if i >1:
        f.append(s[i-2])
    f.append(log(s[i], s[i - 1]))
while '/' in f or '*' in f:
    if '/' in f and '*' in f:
        g = min(f.index('/'), f.index('*'))
    elif '/' in f:
        g=f.index('/')
    elif '*' in f:
        g=f.index('*')
    if f[g]=='*':
        f[g]=float(f[g-1])*float(f[g+1])
        del f[g-1]
        del f[g]
    elif f[g]=='/':
        f[g] = (float(f[g - 1])) / (float(f[g + 1]))
        del f[g - 1]
        del f[g]
    else:
        break


while len(f)>1:
    if f[1]=='+':
        f[1]=float(f[0])+float(f[2])
        del f[0]
        del f[1]
    elif f[1]=='-':
        f[1]=float(f[0])-float(f[2])
        del f[0]
        del f[1]
    else:
        break
print(*f)




