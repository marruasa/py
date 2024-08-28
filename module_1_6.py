my_dict = {'Masha': 23, 'Anya': 25, 'Alice': 24}
print('Dict: '+ str(my_dict))
print('Existing value: '+ str(my_dict['Alice']))
print('Not existing value: '+str(my_dict.get('Katya')))
my_dict.update({'Sofya': 27, 'Sasha': 22})
a = my_dict.pop('Anya')
print('Deleted value: '+str(a))
print('Modified dictionary: '+str(my_dict))

my_set = {1, 1, 1, 'Yes', 'Yes', False, False, False}
print("Set: "+str(set(my_set)))
my_set.add(float(1.5))
my_set.add(tuple((3, 4, 5)))
my_set.discard('Yes')
print("Modified set: "+ str(my_set))