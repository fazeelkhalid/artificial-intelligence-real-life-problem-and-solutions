import copy
set1 = set([1,2,3,4,2,3,5,6])
set2 = set([6,4,3,5,8,78,3,3,2])
set4 = set([100])


#LENGTH
print ('\t\t\tLength of sets')
print('Set1 length : ', len(set1))
print('Set2 length : ', len(set2))

#UNION
print("Union of two sets : ", set1 | set2)

#INTERESECTION
print("Interesection of two sets : ", set1 & set2)

#MAXIMIUM
print("Max value of set1 : ", max(set1))
print("Max value of set2 : ", max(set2))

#MINIMUM

print("Min value of set1 : ", min(set1))
print("Min value of set2 : ", min(set2))

#SHALLOW COPY
set3 = copy.copy(set1)
print('Shallow copy : ', set3)

#SUBSET
if(set1.issubset(set2)):
    print('Set1 is a subset of set2')
else:
    print('Set1 is not a subset of set2')

# remove all elements from a given set
set4 = set([1,2,3,4,2])
set4.clear();

#check if two given sets have no elements in common
if(set1.isdisjoint(set4)):
    print('No elements common')
else:
    print('Some elements are common')

if(set1.issuperset(set2)):
    print('Set1 is a superset of set2 and itself')
else:
    print('Not a superset')
