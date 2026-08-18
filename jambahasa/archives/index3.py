import wasp
import json
import os
directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(directory)

class JambahasaApp():

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
    
    with open("jambahasa_en_id.json", "r", encoding="utf-8") as file:
        enId = json.load(file, object_pairs_hook=groupDuplicateKeys)

    with open("jambahasa_id_en.json", "r", encoding="utf-8") as file:
        idEn = json.load(file, object_pairs_hook=groupDuplicateKeys)

    # print(idEn["bodoh"])
    '''with open("id-en.json", "w", encoding="utf-8") as file:
        json.dump(idEn, file, indent=4)'''
