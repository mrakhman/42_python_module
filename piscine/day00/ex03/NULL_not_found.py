def NULL_not_found(object: any) -> int:
    name = ''

    match object:
        case None:
            name = 'Nothing'
        case float("NaN"):
            name = 'Cheese'
        case 0:
            name = 'Zero'
        case '':
            name = 'Empty'
        case False:
            name = 'Fake'
        case _:
            name = 'Cheese'

    try:
        object_type = type(object)
        if object == 'Brian':
            print('Type not Found')
        else:
            print(name, ':', object, object_type)
        return 1
    except Exception:
        return 0

# # Copy that to tester.py:
# from NULL_not_found import NULL_not_found

# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ''
# Fake = False

# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))
