'''
Created on Apr 24, 2018

@author: ankusain
'''
n=22
a = int(input('Guess a number between 1 - 100: '))
if a < 0 or a > 100:
    print ('Please pick a value with in a range')
if n == a:
    print ('Congratulations')
elif a < 22:
    print ('Guess Higher')
elif a > 22:
    print ('Guess Lower')
    