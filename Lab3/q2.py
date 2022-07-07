print('Please enter string')
string = input()
count = 0
vowelSet = set(['a','e','i','o','u','A','E','I','O','U'])
for i in string:
    if(i in vowelSet):
        count = count + 1

print('Vowels No : ', count)





















