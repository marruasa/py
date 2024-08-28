immutable_var = 1, 'b', True
print('Immutable tuple: '+str(immutable_var))
# значения кортежа 'immutable_var' нельзя изменить, т.к. он является неизменяемым объектом как строка или число
mutable_list = [1, 2, 3, 4, 5]
mutable_list[1] = 'A'
mutable_list[-1] = False
mutable_list.remove(4)
mutable_list.append('Apple')
print('Mutable list: '+str(mutable_list))