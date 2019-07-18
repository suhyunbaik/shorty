# Shorty
## Overview
Shorty is a test project. 

## Technical info
* Python 3.7.2
* Flask
* RESTful API
* SQLAlchemy
* Mysql
* Alembic

## Installation / Setup
1. clone repository
``` git clone git@github.com:suhyunbaik/shorty.git```

2. install pyenv virtualenv(Optional)
```pyenv virtualenv 3.7.2 [environment name]```

3. install dependencies
```pip3 install -r requirements.txt```

4. set environment variable
```export SHORTY_ENV=local```

5. run alembic
```alembic upgrade head```

6. run project
```python run.py```

6. visit `127.0.0.1:5000` to use the app

