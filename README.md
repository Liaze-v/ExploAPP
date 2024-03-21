<br/>
<p align="center">
  <h3 align="center">ExploAPP</h3>

  <p align="center">
    A Better explorator and search file on Windows with TAG
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)

## About The Project

![Screen Shot](images/screenshot.png)

There are several solutions for file exploration but I couldn't find anything simple.

Especially a way to quickly search by name or tags in a specific folder.

Of course this project needs a lot of improvement. But it's perfect for creating tags and searching for files.


## Built With

This project is built with python and flask for the server side. For a more modern interface, it uses HTMLX and TailwindCSS for styling.

## Getting Started

You can simply go to the dist folder and copy ExploApp.exe, then paste it into the folder you want.

Alternatively, copy the files

### Prerequisites

Prerequisites python 3.9

Create env
python -m venv .venv

Enabled env
.venv\Scripts\activate

### Installation

pip install Flask
pip install flaskwebgui
pip install psutil
pip install -U pyinstaller

The Build command is
pyinstaller --name="ExploApp" --noconsole --onefile --path=env\lib\site-packages --add-data="static;static" --add-data="templates;templates" main.py

For continue development



## Usage

You can copy and paste ExploAPP.exe into any folder. It's designed to be portable

The application will list every file in the current folder or subfolder.

When you launch the application for the first time, a new folder will be created, a new ExploApp folder. The sole purpose of this folder is to create a JSON file containing a list of your files, in order to reduce storage (read) usage. 

You can add tags to your files to facilitate searching and sorting. When you add a tag, the name of your files changes and adds [your tag]. This decision is made in order to preserve tags even if your file changes folder.


To continue the development. 
Go to main.py 
and go to
 if __name__ == "__main__":

add comment
 FlaskUI(app=app, server="flask",width=1400, height=1000).run()
and remove comment
 app.run(debug=True) 