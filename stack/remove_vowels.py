
# Stackoverflow original question 
# http://stackoverflow.com/questions/41324611/why-doesnt-my-loop-work
def anti_vowel(text):
    last = []
    for cha in text:
        last.append(cha)
    for char in last:
        if char == 'a' or char == 'A' or\
        char == 'e' or char== 'E' or\
        char == 'i' or char== 'I' or\
        char == 'o' or char== 'O' or\
        char == 'u' or char== 'U':
            last.remove(char)

    return "".join(last)

print('Original: ', anti_vowel('Hey look Words!'))

# Quick fix
def anti_vowel_quick(text):
    last = []
    for cha in text:
        last.append(cha)
    for char in last[:]: # Added [:] to fix
        if char == 'a' or char == 'A' or\
        char == 'e' or char== 'E' or\
        char == 'i' or char== 'I' or\
        char == 'o' or char== 'O' or\
        char == 'u' or char== 'U':
            last.remove(char)

    return "".join(last)

print("Quick: ", anti_vowel_quick('Hey look Words!'))
print("Quick: ", anti_vowel_quick('Hey lOok WOrds!'))

# Proposed solution
def anti_vowel_fixed(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join(filter(lambda x: x.lower() not in vowels, text))

print('Fixed: ', anti_vowel_fixed('Hey look Words!'))
print('Fixed: ', anti_vowel_fixed('Hey lOok WOrds!'))
