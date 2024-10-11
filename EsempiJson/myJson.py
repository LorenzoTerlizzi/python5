import json
import jsonschema
import requests
import sys

data = {}
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "scores": {
            "type": "array",
            "items": {"type": "number"},
        }
    },
    "required": ["name"],
    "additionalProperties": False
}

def JsonSerialize(data, sFile):
    with open(sFile, "w") as write_file:
        json.dump(data, write_file)

def JsonDeserialize(sFile):
    with open(sFile, "r") as read_file:
        return json.load(read_file)
    
def print_dictionary(dData, sRoot):
    for keys, values in dData.items():
        if sRoot != "":

            print("Trovata chiave " + sRoot + "." + keys)
        else:
            print("Trovata chiave " + keys)
        #print(values)
        #print(type(dData[keys]))
        if type(dData[keys]) is dict:
            if sRoot != "":
                print_dictionary(dData[keys], sRoot + "." + keys)
            else:
                print_dictionary(dData[keys], keys)


api_url = "https://jsonplaceholder.typicode.com/todos/5"
response = requests.get(api_url)
print(response.json())
# print(response.status_code)
# print(response.headers["Content-Type"])
# if(response.status_code==200):
#     if (type(response.json()) is dict):
#         print_dictionary(response.json(), "")
sys.exit()



myFile = "./esempio3.json"
data = JsonDeserialize(myFile)

try:
    jsonschema.validate(data, schema)
    print("L'istanza è coerente con lo schema")
except jsonschema.exceptions.ValidationError:
    print("L'istanza non è valida")



#print_dictionary(data, "")
sys.exit()

print(type(data['quiz']))
if type(data['quiz']) is dict:
    print_dictionary(data['quiz'])

