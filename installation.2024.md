# Installation Guide (2024)

## Environment Setup

Create and activate virtual environment:
```bash
pyenv virtualenv 3.10 recruitment
pyenv activate recruitment
```

Install dependencies:
```bash
pip install -r requirements.txt

# Or use Tsinghua mirror (faster in China)
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Start Local Redis Service

```bash
redis-server
```

## Change Admin User Password

```bash
python manage.py changepassword admin
```

## Start the Service

```bash
python3 ./manage.py runserver 127.0.0.1:8000 --settings=settings.local
```

Login with admin credentials.
