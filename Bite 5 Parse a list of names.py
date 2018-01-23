NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    set_of_names = set()
    for name in names:
        set_of_names.add(name.title())
    return list(set_of_names)



def sort_by_surname_desc(names):
    names = dedup_and_title_case_names(names)
    return sorted(names, key=lambda name: name.split()[1], reverse=True)


def shortest_first_name(names):
    names = dedup_and_title_case_names(names)
    return min(names, key=lambda name: name.split()[0]).split()[0]

print(dedup_and_title_case_names(NAMES))
print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))