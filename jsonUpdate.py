import os
import json
import re
import jsoncreation 

# pathOrigin = "./fakefile"

def datajson(pathOrigin):
    pathJsonFile = pathOrigin+"/ExploApp/jsonApp/data.json"
    JsonFileExists = os.path.isfile(pathJsonFile)
    datajson = []
    if(JsonFileExists == False):
        jsoncreation.creatjson(pathOrigin)
        with open(pathJsonFile, 'r',encoding="utf-8") as infile:
            datajson = json.load(infile)
    else:
        with open(pathJsonFile, 'r',encoding="utf-8") as infile:
            datajson = json.load(infile)
    return datajson
    
def uptdatejson(pathOrigin,pathID,newCustomfilename,newtag):
    pathJsonFile = pathOrigin+"/ExploApp/jsonApp/data.json"
    with open(pathJsonFile, 'r',encoding="utf-8") as infile:
            jsonListOLD = json.load(infile)
    jsonListNEW = []
    AddTofileNameTag = ""
    for i in range(len(jsonListOLD)):
        if(jsonListOLD[i]['path'] == pathID):
            currentTag = []
            for c in newtag:
                if c not in currentTag:
                    currentTag.append(c)
                    continue
            for r in currentTag:
                AddTofileNameTag = AddTofileNameTag + "["+ r + "]"
            jsonListOLD[i]['tag'] = currentTag
            jsonListOLD[i]['customname'] = newCustomfilename
            # namewithouttag1 = re.sub(r"\[([A-Za-z0-9_]+)\]", "", jsonListOLD[i]['name'])
            # namewithouttag2 = re.sub(r"^\s+|\s+$", "", namewithouttag1)
            jsonListOLD[i]['name'] = newCustomfilename+ " " + AddTofileNameTag
            jsonListNEW.append(jsonListOLD[i])
            # Renaming the file
            pathdirname = os.path.dirname(jsonListOLD[i]['path'])
            new_name = pathdirname + "\\" + jsonListOLD[i]['name'] + jsonListOLD[i]['filetype']
            print(new_name)
            os.rename(jsonListOLD[i]['path'], new_name)
            jsonListOLD[i]['path'] = new_name
            continue
        else:
            jsonListNEW.append(jsonListOLD[i])
    pathJsonFile2 = pathOrigin+"/ExploApp/jsonApp/data.json"
    with open(pathJsonFile2, 'w',encoding="utf-8") as outfile:
        json.dump(jsonListNEW, outfile)
        
def refreshjsondata(pathOrigin):
    pathJsonFile = pathOrigin+"/ExploApp/jsonApp/data.json"
    os.remove(pathJsonFile)
    jsoncreation.creatjson(pathOrigin)