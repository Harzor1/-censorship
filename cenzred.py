 

def replace_russian_letters(string):
    replacements = {'р': 'p', 'а': 'a', 'е': 'e', 'к': 'k', 'м': 'm', 'о': 'o', 'с': 'c', 'у': 'y', 'х': 'x', 'и':'u'}
    result = ''
    for char in string:
        if char.lower() in replacements:
            result += replacements[char.lower()] 
        else:
            result += char
    return result
while True:
    input_string = input("Введите текст: ")
    if input_string.lower() == "выход":
        break
    else:       
        print("Результат замены:", replace_russian_letters(input_string))


    