import json

def groupDuplicateKeys(database):
    result = {}
    for key, value in database:
        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value
    return result

with open("en-id.json", "r", encoding="utf-8") as file:
    enId = json.load(file, object_pairs_hook=groupDuplicateKeys)

with open("id-en.json", "r", encoding="utf-8") as file:
    idEn = json.load(file, object_pairs_hook=groupDuplicateKeys)

#print(enId)
#result = enId["talk"]
#result = enId.get("doufu", "sorry, this translation is missing")
#print(result)