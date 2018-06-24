with open('a.txt') as f1 ,open('b.txt') as f2:
    for l1,l2 in zip(f1,f2):
        print(l1+l2)