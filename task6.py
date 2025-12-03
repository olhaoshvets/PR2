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