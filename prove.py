#syntax dictonary - A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# syntax
empty_dict = {}
#Dictionary with data values
dct1 = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
person = {
    'first_name':'Maria',
    'last_name':'Rossi',
    'age':25,
    'country':'Italy',
    'is_marred':False,
    'skills':['JavaScript', 'C', 'Java', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'00000'
     }
    }
#stampa persona
print(person)
#print()

num=int(input("inserisci un valore:"))

#for a in range(1,num):
 #   print(" - ", a)

#stampa un triangolo formato da cancelletti
for b in range (1, 10):
    print(b*'#')


for c in range(1,5):
    
    for d in range (1,5):
        print(d*'*')

    print(c*'#')