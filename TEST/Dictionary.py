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

str(rec)
f = open('/home/corey/test_data.txt', 'w')
f.write(rec[''])
f.close()