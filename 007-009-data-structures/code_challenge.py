cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    items = ", ".join(cars['Jeep'])
    return items


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    items = []
    for k in cars.keys():
        items.append(cars[k][0])
    return items


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    items = []
    for v in cars.values():
        for m in v:
            if grep.lower() in m.lower():
                items.append(m)
    return sorted(items)


def sort_car_models(cars=cars):
    for v in cars.values():
        v.sort()
    return cars


def main():
    get_all_jeeps()
    get_first_model_each_manufacturer()
    get_all_matching_models()
    sort_car_models()


if __name__ == '__main__':
    main()
