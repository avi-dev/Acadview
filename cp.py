f = open('a.txt','r')
f_read = f.readlines()
with open('b.txt','w') as f1:
    for i in f_read:
        f1.write(i)
