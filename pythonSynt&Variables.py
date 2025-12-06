#Task 1
name = 'Olha'
age = 27

print('Hi, my name', name, 'and I am', age, 'years old.')
print('Hi, my name ' + name + ' and I am ' + str(age) + ' years old.')
print('Hi, my name {} and I am {} years old.'.format(name, age))
print(f'Hi, my name {name} and I am {age} years old.')

#Task 2
text = 'Hello World'
print((text + ' ') * 10)

#Task 3
text = 'OMG'
print(text, end='!!!')

#Task 4
first_lang = 'Python'
second_lang = 'Java'
third_lang = 'C++'

print(first_lang, second_lang, third_lang, sep='|',end='!')

#Task 5
a = int(342)
b = float(51.6)

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a *b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

#Task 6
a = float(2.134)
b = float(3.1415)

print('Old values:', a, b)
a, b = b, a
print('New values:', a, b)


print('Old values:', a, b)
temp = a
a = b
b = temp
print('New values:', a, b)

#Task 7
a = int(3)
b = float(0.02)
c = float(75.8)
d = float(-43.2)
e = int(362)

numbers = [a, b, c, d, e]
totalSum = sum(numbers)
count = len(numbers)
average = totalSum / count
print(average)

#Task 8
name = input()
surname = input()

print('My name is', name, surname)

#Task 9
length = int(input())
width = int(input())

print('The area of the rectangle is:', length * width)

#Task 10
x = int(273)
y = int(65)

y += 208
print('Does the first number equal the second one?', x == y, sep=' ')
y -= 1
print('Does the first number greater than the second one?', x > y, sep=' ')
y += 2
print('Does the first number less than the second one?', x < y, sep=' ')
y -= 127
print('Does the sum of the two numbers equal 420?', x + y == 420, sep=' ')

#Task 11
cel = float(input())
F = (cel * 9 / 5) + 32
print('The temperature is', cel, 'C. In Fahrenheit it is', F, 'F.')