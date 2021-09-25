def calculate(number):
    if number %3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    elif '7' in str(number):
        print('Github')
    else:
        print(number)

for i in range(20):
    calculate(i)
    
