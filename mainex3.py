from src import ex3

def main():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
]
    new_people_list = ex3.calc_bmi(people_list)

if __name__ == '__main__':
    main()