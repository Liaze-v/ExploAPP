import os
import json
import re

# pathorigin lieu du commencement
# pathOrigin = "./fakefile"


def normalizeName(customname):
    customname = customname.replace("_", " ")
    customname = customname.replace("-", " ")
    customname = customname.replace(".", " ")
    customname = customname.replace(";", " ")
    # On remplace Ce que contien les  []
    customname = re.sub('/\[.*?\]/g',"",customname)
    # On remplace Ce que contien les  ()
    customname = re.sub('/\(.*?\)/g',"",customname)
    # On Trim les espace devant et a la fi
    customname = re.sub('/^\s+|\s+$/gm',"",customname)
    # On Trim les double espace
    # customname = re.sub(' {2,}'," ",customname)
    customname = customname.title()
    return customname


def scanFile(pathOrigin):
    itemtoappend = []
    imageDefault = [
        [".txt", "file-txt.svg"],[".mp3", "file-mp3.svg"],
        [".mp4", "file-mp4.svg"],[".pdf", "file-pdf.svg"],
        [".jpg", "file-jpg.svg"],[".png", "file-png.svg"],
        [".csv", "file-csv.svg"],[".ppt", "file-ppt.svg"],
        [".zip", "file-zip.svg"],[".xls", "file-xls.svg"],
        [".js", "file-javascript.svg"],[".iso", "file-iso.svg"],
        [".exe", "file-exe.svg"],[".doc", "file-doc.svg"],
        [".rar", "file-rar.svg"],[".epub", "file-epub.svg"]
        ]
    tags = []
    for dirPath, dirNames, fileNames in os.walk(pathOrigin):
        if(dirPath == pathOrigin+"\ExploApp"):
            break
        print("Directory Path: ", dirPath)
        print("Directories = ", dirNames)
        print("Files = ", fileNames)
        print('-' * 10)
        for fileName in fileNames:
            if(fileName == "ExploApp.exe"):
                continue
            pathfile = os.path.join(dirPath, fileName)
            name = os.path.splitext(fileName)[0]
            customname = re.sub(r"\[(?<=\[).+?(?=\])\]", "", name)
            tags = re.findall(r"(?<=\[).+?(?=\])", name)
            # tags = re.findall(r"\[([A-Za-z0-9_]+)\]", name)
            print(name)
            print(customname)
            print(tags)
            filetype = os.path.splitext(fileName)[1]
            for item in imageDefault:
                if(item[0] == filetype):
                    pathimg = item[1]
                    break
            else:
                pathimg = "file-default.svg"
            itemtoappend.append({"name": name, "customname": normalizeName(customname),"tag" : tags, "path": pathfile, "pathimg": pathimg, "filetype": filetype})
    jsonList = json.dumps(itemtoappend, indent=4)
    return jsonList

def creatjson(pathOrigin):
    creatfileneed(pathOrigin)
    pathJsonFile = pathOrigin+"/ExploApp/jsonApp/data.json"
    jsonList = scanFile(pathOrigin)
    with open(pathJsonFile, "w",encoding="utf-8") as outfile:
        outfile.write(jsonList)
        
def creatfileneed(pathOrigin):
    pathDossierApp = pathOrigin+"/ExploApp"
    pathImage = pathDossierApp+"/imagesApp"
    pathJson = pathDossierApp+"/jsonApp"
    DossierAppdirExists = os.path.isdir(pathDossierApp)
    if(DossierAppdirExists == False):
        os.mkdir(pathDossierApp)
    imagedirExists = os.path.isdir(pathImage)
    if(imagedirExists == False):
        os.mkdir(pathImage)
    JsondirExists = os.path.isdir(pathJson)
    if(JsondirExists == False):
        os.mkdir(pathJson)
