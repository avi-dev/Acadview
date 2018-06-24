a=3
if a<4:
    try:
        b=a/(a-3)
        print(b)
    except ZeroDivisionError as e:
        print(e)