# Flask Template Project
This project is to test out my local Kubernetes setup and refresh some Flask.

# Notes
## Scaffolding
- initialize project with Poetry
  ```
  mkdir todo-flask-app
  cd todo-flask-app
  poetry init
  poetry add flask
  ```
- create Flask app
  - linux
    ```bash
    NAME="todo-flask-app"

    mkdir -p "$NAME/static/css"
    mkdir -p "$NAME/static/js"
    mkdir -p "$NAME/templates"

    touch "$NAME/static/css/styles.css"
    touch "$NAME/static/js/script.js"
    touch "$NAME/templates/index.html"
    touch "$NAME/app.py"
    touch "$NAME/models.py"

    ```
  - windows (batch)
    ```batch
    set "NAME=todo-flask-app"

    mkdir "%NAME%\static\css"
    mkdir "%NAME%\static\js"
    mkdir "%NAME%\templates"

    type nul > "%NAME%\static\css\styles.css"
    type nul > "%NAME%\static\js\script.js"
    type nul > "%NAME%\templates\index.html"
    type nul > "%NAME%\app.py"
    type nul > "%NAME%\models.py"
    ```
  - windows (powershell)
    ```powershell
    $NAME = "todo-flask-app"
    New-Item -Path "$NAME\static\css" -ItemType Directory
    New-Item -Path "$NAME\static\js" -ItemType Directory
    New-Item -Path "$NAME\templates" -ItemType Directory
    
    New-Item -Path "$NAME\static\css\styles.css" -ItemType File
    New-Item -Path "$NAME\static\js\script.js" -ItemType File
    New-Item -Path "$NAME\templates\index.html" -ItemType File
    New-Item -Path "$NAME\app.py" -ItemType File
    New-Item -Path "$NAME\models.py" -ItemType File
    ```
- create Dockerfile (check you use the same python version)
- create Models - `models.py`
- create Views + Controllers - `app.py`

## Deployment
- deploy to Railway 
- deploy via Harness to Kubernetes on home server

