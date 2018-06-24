l = [1,2,3]
try:
    print(l[3])
except IndexError as e:
    print(e)