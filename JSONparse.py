import json

with open("craftable_items.json") as fname:
    data = json.load(fname)

first = data[0]

newJson = {}
name = ""

for key in data:
    for i in key:
        if i == "station":
            station = key.get(i)
        if i == "craftable":
            for craft in key.get(i):
                name = craft.get('name')
                newJson[name] = {}

                level = craft.get("level")
                newJson[name]['level'] = int(level[-1])

                time = craft.get('time').split('\n')
                newJson[name]['time'] = time[1]

                mults = [char for char in craft.get('mults') if char.isdigit()]

                newJson[name]['num_crafted'] = mults[0]

                newJson[name]['craftable_img'] = craft.get('craftable_img')

                newJson[name]['station'] = station

                matList = craft.get('materials')
                for mat in range(len(matList)):
                    matList[mat]['mult'] = int(mults[mat])
                    matList[mat].pop('url', None)
                    matList[mat].pop('mat_img_url', None)
                newJson[name]['materials'] = matList



                # for j in craft:                 # j is all the keys in "craftable"
                #     if j == 'name':
                #         name = craft.get(j)
                #         newJson[name]["name"] = name
                #     if j == 'level':
                #         newJson[name]["level"] = j
                #     if j == 'time':
                #        time = j
                #        time.split('\n')
                #        newJson[name]["time"] = time[1]
                #     if j == 'materials':
                #         #print(craft.get(j))     # when j == mats -> [{mats}]
                #         newJson[name]["materials"] = craft.get(j)

with open("fixed.json", 'w') as f:
    json.dump(newJson, f)
