import json

def to_save_json(dic,fp):
    with open(fp,mode="w") as f:
        json.dump(obj=dic, fp=f)
    print("dict save done")