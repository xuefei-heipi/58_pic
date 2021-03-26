
def t():
    try:
        for i in range(1, 200):
            if i == 30:
                raise ValueError("shicuo")
            print(i)
    except ValueError as E:
        print(E)
    except Exception as E:
        print(E)
        return None

    print('21212')

t()

