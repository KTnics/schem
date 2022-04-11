from pickle import FALSE, TRUE
from jsonschema import Draft7Validator
from json import load

with open('schema.json') as f:
    schema = load(f)

list_ = [
    { "oneOf": [
  { "required": [  {'name': 'nikhil', 'id':12,'govid': 1245678004, 'cell':12345678, 'phone':1231231234,'birthday':'19/08/98' ,'day': 'su' }] },
 
  { "not":
    { "anyOf": [
      { "required": [ {'name': 'nikhil', 'id':12,'govid': 1245678004, 'cell':12345678, 'phone':1231231234,'birthday':'19/08/98' ,'day': 'su' }] },
     
    ] }
  }
] },
  
 
]

validator = Draft7Validator(schema)
assert validator.is_valid(list[0]) is TRUE
  
  

assert validator.is_valid(list[1]) is FALSE

print(list(validator.iter_errors(list_)))