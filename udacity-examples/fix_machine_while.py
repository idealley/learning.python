# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# TOOLS: if statement
         # while loop
         # string operations
         # Unit 1 Basics

def fix_machine(debris, product):
    result = ''
    i = 0
    while i <= len(product)-1:
        if(product[i] in debris):
            result += product[i]
        i += 1    
    if result != product:
        return "Give me something that's not useless next time."
    return product    


print("Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity'))
print("Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity'))
print("Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity'))
print("Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt'))