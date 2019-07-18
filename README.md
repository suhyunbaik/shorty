# Shorty
단축 url 생성

## Technical info
* Python 3.7.2
* Flask
* RESTful API
* SQLAlchemy
* Mysql
* Alembic

## Installation / Setup
1. 리포지토리 클론
``` git clone git@github.com:suhyunbaik/shorty.git```

2. pyenv virtualenv 설치 (옵션)
```pyenv virtualenv 3.7.2 [environment name]```

3. 패키지 설치
```pip3 install -r requirements.txt```

4. 환경변수 설정
```export SHORTY_ENV=local```

5. alembic 실행해서 테이블 create
```alembic upgrade head```

6. 프로젝트 실행
```python run.py```

6. 브라우저에 `127.0.0.1:5000` 
또는 포스트맨에 `127.0.0.1:5000/urls` 주소로 접속

