def count_calls():
    global calls
    calls += 1


def string_info(string_:str):
    count_calls()
    tuple_ = (len(string_), string_.upper(), string_.lower())
    return tuple_


def is_contains(string_:str, list_to_search:list):
    count_calls()
    for i in range(len(list_to_search)):
        if type(list_to_search[i]) == str:
            list_to_search[i] = str(list_to_search[i]).lower()
    if string_.lower() in list_to_search:
        return True
    else:
        return False

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
