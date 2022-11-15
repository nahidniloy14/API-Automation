import json
courses = '{"name": "RahulShetty","languages": [ "Java", "Python"]}'
#the courses is a string and it is holding our JSON variable

#Loads method parse json string and it returns dictionary
#json.loads(courses)
dictionary_courses=json.loads(courses)
print(type(dictionary_courses))
# type will tell us the data type which we passed inside it
#output: <class 'dict'>
print(dictionary_courses)
#output: {'name': 'RahulShetty', 'languages': ['Java', 'Python']}
# 'name' and 'languages' are key and 'RahulShetty' 'Java' 'Python' is the value
# 'RahulShetty' is a string and ['Java', 'Python'] is a list
print(dictionary_courses['name'])
#output: RahulShetty
list_languages=dictionary_courses['languages']
print(list_languages)
#output: ['Java', 'Python']
print(list_languages[0])
#output: Java

with open('C:\\Users\\lm\\OneDrive - American International University-Bangladesh\\Desktop\\RestAPI\\sampleJSON1.json') as f:
    data=json.load(f)
    print(data)
    #output:{'dashboard': {'purchaseAmount': 910, 'website': 'nahidniloy894@gmail.com'}, 'courses': [{'title': 'selenium', 'price': 50, 'copies': 6, 'details': {'site': 'htttps://www.google.com'}}, {'title': 'Postman', 'price': 14, 'copies': 2}, {'title': 'RestAPI', 'price': 10, 'copies': 8}]}
    print(type(data))
    #<class 'dict'>
    print(data['courses'])
    #[{'title': 'selenium', 'price': 50, 'copies': 6, 'details': {'site': 'htttps://www.google.com'}}, {'title': 'Postman', 'price': 14, 'copies': 2}, {'title': 'RestAPI', 'price': 10, 'copies': 8}]
    print(data['courses'][1])
    #{'title': 'Postman', 'price': 14, 'copies': 2}
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
    for i in data['courses']:
        #print(i)
        #>>{'title': 'selenium', 'price': 50, 'copies': 6, 'details': {'site': 'htttps://www.google.com'}}
        #{'title': 'Postman', 'price': 14, 'copies': 2}
        #{'title': 'RestAPI', 'price': 10, 'copies': 8}
        #price of postman
        if i['title']=='Postman':
            print(i['price'])
            #>>14
            assert i['price'] == 14

