import json
with open("users (2).json","r") as f:
    new_lst = []
    data = json.load(f)
    for i in data:
        if i["is_active"] == True:
            new_lst.append(i)
with open("user.txt","w") as f2:
    json.dump(new_lst,f2,indent=3)



