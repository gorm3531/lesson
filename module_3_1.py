calls = 0


def count_calls(call):
    global calls
    calls += call
    return calls

def string_info(string):
    string_ = []
    string_.append(len(string))
    string_.append(string.upper())
    string_.append(string.lower())
    count_calls(1)
    return tuple(string_)


def is_contains(string_info, is_contains):
    is_contains_2 = []
    count_calls(1)
    string_info.lower()
    for i in is_contains:
        is_contains_2.append(i.lower())
    return (string_info.lower() in is_contains_2)





print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)