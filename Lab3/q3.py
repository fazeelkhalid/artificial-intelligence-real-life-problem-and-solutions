n1 = 10
n2 = 0

print ('Sum : ', n1+ n2)
print ('Diff : ', n1- n2)
print ('Sum : ',n1* n2)

try:
    print('Div : ',n1/n2)
except ZeroDivisionError:
    print("Infinity")
