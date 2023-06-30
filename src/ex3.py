import math

def transform_person(person):
    retval = {
        'id' : person['id'],
        'firstname' : person['name'],
        'weight' : person['weight_kg'],
        'height' : person['height_meters'],
        'bmi' :  round(person['weight_kg'] / person['height_meters'] ** 2, 1)
    }
    return retval

def calc_bmi(people_list):
    new_list = list(map(transform_person, people_list))
    print(new_list)



