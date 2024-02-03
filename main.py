f = open('products.csv', encoding = "UTF8").read()
f = f.split('\n')
a = []
for i in f:
    a.append(i.split(';'))
for el in a:
    el.append('0')
    if "0" in el[5]:
        el[5] = str(float(el[3])*float(el[4]))
print(a)



