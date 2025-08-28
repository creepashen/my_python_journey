def average_age_above_30(value):
    total = 0
    total_names = 0
    
    for names, age in value.items():
       
        if age > 30 :
            total += age
            total_names +=1

    
    return total / total_names

value = {
    'nawaf': 42,'fahad': 36,'majd': 21,
    'sara': 48,'ali': 30,'reem': 27,
    'khaled': 50,'mona': 40,'abdullah': 33,'huda': 45
}

print(average_age_above_30(value))
