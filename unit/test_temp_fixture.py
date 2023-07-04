import json
import os
from tuto_1.temp_fixture import to_save_json

def test_to_save_json(tmpdir,capsys):
    p=os.path.join(tmpdir,"temp.json")
    print(p)
    dic={"name":"sathish"}
    to_save_json(dic, p)
    with open(p,"r") as f:
        dic_load=json.load(f)
    assert dic == dic_load 
    assert capsys.readouterr().out == "dict save done\n"