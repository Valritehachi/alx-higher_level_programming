#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    new_dict = {}
    for key in list(a_dictionary):
        new_dict[key] = a_dictionary[key] * 2
    return new_dict

#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    max_key = max(a_dictionary, key=a_dictionary.get)
    return max_key

# Example usage:
my_dictionary = {"John": 90, "Alice": 85, "Bob": 95}
result = best_score(my_dictionary)
print(result)

