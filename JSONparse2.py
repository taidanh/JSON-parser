import json

with open("craftable_items.json") as fname:
    data = json.load(fname)

first = data[0]

newJson = {"recipes": []}
name = ""

for key in data:
    for i in key:
        if i == "station":
            station = key.get(i)
        if i == "craftable":
            for craft in key.get(i):
                name = craft.get('name') 

                singular = {}

                singular['name'] = name

                level = craft.get("level")
                singular['level'] = int(level[-1])

                time = craft.get('time').split('\n')
                singular['time'] = time[1]
                
                num_crafted = craft.get("num_craftables").split("\n")
                num_crafted = num_crafted[0]
                singular['num_crafted'] = int(num_crafted[1:])
                
                mults = [char for char in craft.get('mults') if char.isdigit()]

                

                singular['craftable_img'] = craft.get('craftable_img')

                singular['station'] = station

                matList = craft.get('materials')
                for mat in range(len(matList)):
                    matList[mat]['mult'] = int(mults[mat])
                    matList[mat].pop('url', None)
                    matList[mat].pop('mat_img_url', None)
                singular['materials'] = matList

                newJson["recipes"].append(singular)

with open("new.json", 'w') as f:
    json.dump(newJson, f)
