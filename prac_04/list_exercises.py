numbers=[]
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
for i in range(0,5):
    user_input = input("Number:")
    number = int(user_input)
    numbers.append(number)

print("The first number is",numbers[0])
print("The last number is",numbers[-1])
print("The smallest number is",min(numbers))
print("The largest number is",max(numbers))
print("The average is",sum(numbers)/len(numbers))

username=input("Enter your name:")
if username in usernames:
    print('Acess granted')
else: print('Access Denied')