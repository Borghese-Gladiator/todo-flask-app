# Flask Template Project
This project is to test out my local Kubernetes setup and refresh some Flask.

## Setup
- `poetry install`
- `poetry run python .\todo-flask-app\app.py`

# Notes
## To Do
- [x] write CRUD endpoints with Flask, Flask-SQLAlchemy + SQLite database (comes default with Python)
- [ ] validate CRUD with Insomnia
  - fix blueprint to register properly
  - fix to run create table for SQLite
  - fix returning SQLAlchemy results in: `TypeError: Object of type Todo is not JSON serializable`
- [ ] add caching (Flask-Caching) - https://flask-caching.readthedocs.io/en/latest/
- [ ] add rate limiting (Flask-Limiter) - https://medium.com/analytics-vidhya/how-to-rate-limit-routes-in-flask-61c6c791961b
- [ ] add performance testing - https://code.likeagirl.io/performance-testing-in-python-a-step-by-step-guide-with-flask-e5a56f99513d
- [X] generate OpenAPI YAML => DONE, used ChatGPT
- [ ] remove usage of flask-sqlalchemy and use SQLAlchemy base models instead
- [ ] move api blueprint to its own file
- [ ] automatically generate openapi YAML documentation
- [ ] deploy to render.com
- [ ] deploy via Harness to Kubernetes on home server

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
- create GitHub Action to build image and push to DockerHub
  - create DockerHub repository to store images
  - create DockerHub access token
  - go to GitHub repository | Settings | Secrets and variables | Actions | click "New repository secret"
    - `DOCKERHUB_USERNAME: <value>`
    - `DOCKERHUB_TOKEN: <value>`
  - linux
    ```
    mkdir -p .github/workflows
    touch .github/workflows/build_and_push.yaml
    ```
  - windows (batch)
    ```
    mkdir .github\workflows
    type nul > .github\workflows\build_and_push.yaml
    ```
  - windows (powershell)
    ```
    New-Item -ItemType Directory -Path .github\workflows
    New-Item -ItemType File -Path .github\workflows\build_and_push.yaml
    ```
- create Kubernetes manifests in kubernetes/ using Docker Image name
  - linux
    ```
    mkdir kubernetes
    touch kubernetes\build_and_push.yaml
    touch kubernetes\ingress.yaml
    touch kubernetes\service.yaml
    ```
  - windows (batch)
    ```
    mkdir kubernetes
    type nul > kubernetes\build_and_push.yaml
    type nul > kubernetes\ingress.yaml
    type nul > kubernetes\service.yaml
    ```
  - windows (powershell)
    ```
    New-Item -ItemType Directory -Path kubernetes
    New-Item -ItemType File -Path kubernetes\deployment.yaml
    New-Item -ItemType File -Path kubernetes\ingress.yaml
    New-Item -ItemType File -Path kubernetes\service.yaml
    ```
