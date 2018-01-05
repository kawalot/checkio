cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated list of jeep models (original order)"""
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    l = []
    for _, v in cars.items():
        l.append(v[0])
    return l


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    l = []
    for car in cars:
        for model in cars[car]:
            case_insensitive_model = model.lower()
            if grep.lower() in case_insensitive_model:
                l.append(model)
    return sorted(l)


def sort_dict_alphabetically():
    """sort both keys and values of cars returning resulting dict"""
    for k, v in cars.items():
        cars[k].sort()
    return cars

print(get_all_jeeps())
print(get_first_model_each_manufacturer())
print(get_all_matching_models(grep='trail'))
print(sort_dict_alphabetically())