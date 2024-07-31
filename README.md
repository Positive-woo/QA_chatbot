# FASTAPI PROJECT TEMPLATE

## Virtual Environment: pipenv
로컬 개발 시 root 폴더에서 `pipenv shell`를 입력하면 `.env`파일의 `PIPENV_VENV_IN_PROJECT=1` 설정에 따라 프로젝트 폴더 내에 가상환경 폴더를 생성

## Formatter
[Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

## Logging
[Rich logging handler](https://rich.readthedocs.io/en/stable/logging.html)

## Project 구조
```
📦poroject root
 ┣ 📁.venv (virtual environments)
 ┣ 📂fastapi
 ┃ ┣ 📂apis
 ┃ ┃ ┣ 📂v1
 ┃ ┃ ┃ ┗ 📜some_api.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂cores
 ┃ ┃ ┣ 📜commons.py
 ┃ ┃ ┣ 📜config.py
 ┃ ┃ ┗ 📜logger.py
 ┃ ┣ 📂databases
 ┃ ┃ ┣ 📂dao
 ┃ ┃ ┃ ┗ 📜some_dao.py
 ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┗ 📜models.py
 ┃ ┣ 📂schemas
 ┃ ┃ ┗ 📜some_schema.py
 ┃ ┣ 📂services
 ┃ ┃ ┗ 📜some_service.py
 ┃ ┗ 📜main.py
 ┣ 📂(volume)
 ┃ ┗ 📂(log)
 ┃    ┗ 🧾(logfile.log)
 ┣ ⚙️(.env)
 ┣ ⚙️.env_sample
 ┣ 🧾.gitignore
 ┣ 🐋docker-compose.yml
 ┣ 🐋Dockerfile
 ┣ ⚙️Pipfile
 ┣ ⚙️Pipfile.lock
 ┗ 🧾README.md
```

## 실행
* root 폴더에서 가상환경을 활성화
    ```bash
    pipenv shell
    ```
* main.py 파일 실행
    ```bash
    python fastapi/main.py
    ```