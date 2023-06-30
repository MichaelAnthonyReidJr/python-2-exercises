def get_people(people_list):
    new_list = [person['name'] for person in people_list if person['age'] >= 15]
    return new_list
