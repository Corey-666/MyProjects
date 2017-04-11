import os

rec = {}

rec['name'] = input('Enter your name ')
#if rec['name'] == '':
#print('Name not entered!')
#rec['name'] = input('Enter your name ')
rec['job'] = str(input('Enter your job '))
rec['age'] = str(input('Enter your age '))

print(rec['name'],
      rec['job'],
      rec['age'])
print(rec)

with open('/home/corey/test_data.txt', 'w') as f:
      f.write(str(rec))


