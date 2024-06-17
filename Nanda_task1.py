Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list=[1,2,3,4,5,6]
>>> my_list.append(7)
>>> my_list.remove(5)
>>> my_list[0]
1
>>> print(my_list)
[1, 2, 3, 4, 6, 7]
>>> my_dict={'name': 'nanda', 'age': '20', 'city': 'goa'}
>>> my_dict['gender']='female'
>>> del my_dict['age']
>>> my_dict['city']='Bangalore'
>>> print('updated dictonary:', my_dict)
updated dictonary: {'name': 'nanda', 'city': 'Bangalore', 'gender': 'female'}
>>> my_set={1,2,3,4,5,6}
>>> my_set.add(7)
>>> my_set.remove(3)
>>> my_set.discard(2)
>>> my_set.add(10)
>>> print('updated set:',my_set)
updated set: {1, 4, 5, 6, 7, 10}
