def print_details(persons_list):
    result = []
    for person in persons_list:
        if person[1] >= 18 and person[2] == "active":
            result.append(person[0])
    return result

person_list = [
    ["Dan", 25, "active"],
    ["Noa", 16, "active"],
    ["Yael", 30, "inactive"],
]

def valid_user_email(user_email):
    if
