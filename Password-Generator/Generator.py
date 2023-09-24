import random

chars = 'abcdefghijklmnñopqrstuvwxyz1234567890!@#$&*'
longitud = 12

password = ''
for x in range(longitud):
    password += random.choice(chars)

print('Password Generate: '+password)
