# khanto_api


## Requirements
* Python 3.9
* MySQL
* Create `.env` file using `.env.example`

## How to run
* Create a new virtualenv:
```
virtualenv venv
```
* Activate virtualenv:
```
source ./venv/bin/activate
```

* Install dependencies:
```
pip install -r requirements.txt
```

* Create new database:

```
CREATE DATABASE khanto_api;
```

* Configure database in `.env`

* Load initial data:

```
python manage.py loaddata v1/fixtures/initial_data.json

```

## Run:
``` 
python manage.py runserver 
```

## Tests:
``` 
python manage.py test
```
