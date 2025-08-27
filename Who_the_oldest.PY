def old_person(x):
   
    _old = 0 
    _name = ''
    for name,age in x:
        
        if age >= _old:
            _old = age
            _name = name
    
    print('The oldest doo in this list is ->',_name,
          '\nhe is ', _old, 'years old')
        
value = {'nawaf': 42,'fahad': 36,'majd': 21,
    'sara': 48,
    'ali': 30,
    'reem': 27,
    'khaled': 50,
    'mona': 40,
    'abdullah': 33,
    'huda': 45}

old_person(value.items())
