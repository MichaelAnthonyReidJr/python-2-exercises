def sort_people(people_list):
    # sort people by id in ascending order
    people_list.sort(key=lambda person: person['id'], reverse = False)
    return(people_list)