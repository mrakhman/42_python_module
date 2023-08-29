ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")  # can be updated only converted to list
ft_set = {"Hello", "tutu!"}  # special methods to update
ft_dict = {"Hello": "titi!"}  # value updated by key

ft_list[1] = 'World!'

ft_tuple_tmp = list(ft_tuple)
ft_tuple_tmp[1] = 'France!'
ft_tuple = tuple(ft_tuple_tmp)

ft_set.discard('tutu!')
ft_set.add('Paris!')

ft_dict['Hello'] = '42Paris!'

print(ft_list)
print(ft_tuple)
print(ft_set)  # set does not preserve elements order
print(ft_dict)
