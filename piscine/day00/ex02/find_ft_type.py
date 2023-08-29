def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    object_str = str(object_type)[8:-2].capitalize()

    if object == 'Brian':
        print('Brian is in the kitchen :', object_type)
    elif object == 10:
        print('Type not found')
    else:
        print(object_str, ':', object_type)
    return 42


# # Copy that to tester.py:
# from find_ft_type import all_thing_is_obj

# ft_list = ["Hello", "tata!"]
# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello": "titi!"}

# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("Brian")
# print(all_thing_is_obj(10))
