# lst = []
# json_data1 = '{"name": "Alice", "age": 25}'
# json_data2 = '{"name": "Bob", "age": 30}'
# a = json.loads(json_data1)
# b = json.loads(json_data2)
# lst.append(a)
# lst.append(b)




# d = json.dumps(lst)
# print(d)

# json_data = '''
# {
#     "company": "TechCorp",
#     "employees": [
#         {"name": "John", "age": 28, "role": "Developer"},
#         {"name": "Jane", "age": 32, "role": "Manager"},
#         {"name": "Mike", "age": 26, "role": "Designer"}
#     ]
# }
# '''
# import json
# a = json.loads(json_data)
# b = a['employees']
# for dc in b:
#     print(f'{dc["name"]} : {dc["role"]}')



# import json
# json_data = '''
# [
#     {"product": "Laptop", "price": 1200},
#     {"product": "Phone", "price": 800},
#     {"product": "Tablet", "price": 300},
#     {"product": "Monitor", "price": 150}
# ]
# '''
# import json
# lst = json.loads((json_data))
# a = 0
# for dc in lst:
#     a += dc['price']
# print(a)



import json

json_data = '''
    {"name": "Alice",
    "age": 25,
    "city": "New York",
    "hobby": "painting"}'''

a = json.loads(json_data)

if "country" not in a:
    a['country'] = "Việt Nam"


print(a)