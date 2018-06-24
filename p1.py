f = open('a.txt','r')
f_read = f.readlines()
f_display = [lines.strip() for lines in f_read]
for i in f_display:
    print(i)
f.close()