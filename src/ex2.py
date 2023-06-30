def filter_males(people_list):
    # males_list = list(filter(lambda person : person['sex'] == 'male', people_list))
    males_list = [person for person in people_list if person['sex'] == 'male']
    return(males_list)
    