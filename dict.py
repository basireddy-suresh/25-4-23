dict={
    "name":"suri",
    "id":51,
    "Branch":"CSD"
}
print(type(dict))
print(dict)
dict["name"]="basireddy"
print(dict)
updated={
    "id":21
}
dict.update(updated)
print(dict)
"""<class 'dict'>
{'name': 'suri', 'id': 51, 'Branch': 'CSD'}
{'name': 'basireddy', 'id': 51, 'Branch': 'CSD'}
{'name': 'basireddy', 'id': 21, 'Branch': 'CSD'}"""