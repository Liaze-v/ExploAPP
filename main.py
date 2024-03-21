from flask import Flask
from flask import render_template
from flask import request
from flask import Flask, redirect, url_for
from flaskwebgui import FlaskUI # import FlaskUI
import os
import jsoncreation
import jsonUpdate
import subprocess


app = Flask(__name__)
# pathOrigin fortest
# pathOrigin = "./fakefile"
# pathOrigin for production
pathOrigin = "./"
 
@app.route("/")
def hello():  
    return render_template('index.html')
  
@app.route("/appstart")
def appstart():  
    return render_template('appstart.html')

@app.route("/oppenfilelocation")
def oppenfilelocation():
    qfilelocation = request.args.get('filelocation')
    filelocation = qfilelocation.replace("/","\\")
    subprocess.Popen(f'explorer /n,/select,{filelocation}')
    return ('', 204)

@app.route("/search",methods= ["POST","GET"])
def search():  
    # input = request.form.get('data')
    # output = request.form.to_dict()
    # data = output['data']
    search = request.args.get('search')
    type = request.args.get('type')
    tag = request.args.get('tag')
    if search == None:
      search=""
    if type == None:
      type=""
    if tag == None:
      tag=""
    return render_template('search.html', search = search, type = type, tag = tag)

@app.route("/datajson",methods= ["POST","GET"])
def datajson():
  # datajsonRender get json data
  datajsonRender = jsonUpdate.datajson(pathOrigin)
  datajsonRenderFiltred = []
  datajsonRenderFiltredbysearch = []
  datajsonRenderFiltredbytype = []
  qsearch = request.args.get('search')
  if qsearch:
    for data in datajsonRender:
      if qsearch.lower() in data["name"].lower() or qsearch.lower() in data["customname"] or qsearch.lower() in data["tag"]:
        datajsonRenderFiltredbysearch.append(data)
  else:
    datajsonRenderFiltredbysearch = datajsonRender
  # if type => datajsonRenderFiltredbytype with datajsonRender
  qtype = request.args.get('type')
  if qtype:
    for data in datajsonRenderFiltredbysearch:
      if qtype == data["filetype"]:
        datajsonRenderFiltredbytype.append(data)
  else:
    datajsonRenderFiltredbytype = datajsonRenderFiltredbysearch
  # if tag => datajsonRenderFiltred with datajsonRenderFiltredbytype
  qtag = request.args.get('tag')
  if qtag:
    for data in datajsonRenderFiltredbytype:
      for d in data["tag"]:
        if qtag == d:
          datajsonRenderFiltred.append(data)
  else:
    datajsonRenderFiltred = datajsonRenderFiltredbytype
  # Build Nav file types [".pdf","PDF"]
  fileEndtypes = []
  fileReplacetypes = []
  datajsonRenderType = []
  datajsonRenderTag = []
  # if search true get Type and Tag of search only
  if qsearch:
    datajsonRenderType = datajsonRenderFiltredbysearch
    datajsonRenderTag = datajsonRenderFiltredbytype
  else:
    datajsonRenderType = datajsonRender
    datajsonRenderTag = datajsonRenderFiltredbytype
  for i in datajsonRenderType:
    filePreEndtypes = i["filetype"].replace(".","").upper()
    if filePreEndtypes not in fileReplacetypes:
      fileReplacetypes.append(filePreEndtypes)
      fileEndtypes.append([filePreEndtypes,i["filetype"]])
  # Build Nav file TAG With datajsonRenderFiltredbytype for get all tag
  fileTAGs = []
  for i in datajsonRenderTag:
    for d in i["tag"]:
      if d not in fileTAGs:
        fileTAGs.append(d)
  # for new query change qtype and qtag if None to ""
  if qtype == None:
    qtype=""
  if qtag == None:
    qtag=""
  if qsearch == None:
    qsearch=""
  qnumber = request.args.get('number')
  if qnumber == None:
    qnumber=0
  maxnumber = int(qnumber) + 100
  datajsonRenderFiltredlimited = []
  for i in range(0,maxnumber):
    if i < len(datajsonRenderFiltred):
      datajsonRenderFiltredlimited.append(datajsonRenderFiltred[i])
  return render_template('jsondata.html', results = datajsonRenderFiltredlimited, tabfiletypes = fileEndtypes ,fileTAGs = fileTAGs, qtype = qtype, qtag = qtag, qsearch = qsearch, qnumber = maxnumber) 

@app.route("/newvalue",methods= ["POST","GET"])
def newvalue():
  newtag = []
  newCustomfilename = ""
  pathID = ""
  datafromInput = request.form.to_dict()
  for data in datafromInput:
    if data == "filename":
      newCustomfilename = datafromInput[data]
    elif "tag" in data:
      if datafromInput[data] != "":
        newtag.append(datafromInput[data])
    elif data == "pathID":
      pathID = datafromInput[data]
    elif data == "currentsea":
      search = datafromInput[data]
    elif data == "currentta":
      tag = datafromInput[data]
    elif data == "currenttyp":
      type = datafromInput[data]
  jsonUpdate.uptdatejson(pathOrigin,pathID,newCustomfilename,newtag)
  return redirect(url_for('search',search=search, type=type, tag=tag))

@app.route("/refreshjson",methods= ["POST","GET"])
def refreshjson():
  jsonUpdate.refreshjsondata(pathOrigin)
  return redirect(url_for('appstart'))


if __name__ == "__main__":
  # If you are debugging you can do that in the browser:
  # app.run(debug=True)
  # If you want to view the flaskwebgui window:
  FlaskUI(app=app, server="flask",width=1400, height=1000).run()