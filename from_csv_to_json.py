import json
import random
def add_locations():
    with open("uszips.csv",encoding="utf8") as file:
        file.readline()
        json_out=[]
        id=1
        for line in file.readlines():
            line=line.split(",")
            json_out.append({
                "model":"core.Location",
                "pk":id,
                "fields":{
                    "city":line[3].replace('"',''),
                    "state_name":line[5].replace('"',''),
                    "index":line[0].replace('"',''),
                    "lat":float(line[1].replace('"','')),
                    "lng":float(line[2].replace('"',''))
                }
            })
            id+=1
        for i in range(10,21):
            json_out.append({
                "model":"core.Car",
                "pk":i-9,
                "fields":{
                    "number":f"10{i}A",
                    "location_place":1,
                    "max_weight":1000,

                }
            })
        with open("core/fixtures/mydata.json", "w") as write_file:
            
            json.dump(json_out,write_file,indent=4)

        
add_locations()