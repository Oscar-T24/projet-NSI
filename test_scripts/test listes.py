liste1 = list('bonjour')
liste2 = ['c','u','e','a','b','e','d','r','h']

for i in liste1:
    for e in liste2:
        if i == e or e == i:
            print(i)
