import json

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
