my_dict_ = {'Deniz': 1982, 'ula': 1986,'Semen': 2016}
print(my_dict_)
print(my_dict_['Deniz'])
print(my_dict_.get('Sasha'))
my_dict_.update({'Sasha':456123789,
                   'Alex': 564987321})
del my_dict_['Deniz'] #удаляет из словаря
print(my_dict_['Alex'])
print(my_dict_)
my_set_ = {1,2,3,4,5,6,1,2,3,4,5,6,'string'}  # множество значений
print(my_set_)
(my_set_.add((8,9)))
print(my_set_)
my_set_.remove((1))
print(my_set_)