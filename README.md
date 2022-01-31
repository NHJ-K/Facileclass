#Not Completed

# LMS
My final year college project with <br>
[@Krishnadas](https://github.com/Krishnadas-KD) <br>
[@Yaseen](https://github.com/mhdyazinkc)<br>
[@Nakhilesh](https://github.com/nakhileship)<br>
## Setup Instructions

### Setup Virtual Environment

```bash
pip install virtualenv
py -m venv env
.\env\Scripts\activate
```      

### Install Required Python Modules

```bash
pip install -r requirements.txt
```
### Reset DB

```bash
python manage.py flush
```

### Update Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Web Server

```bash
python manage.py runserver
```
