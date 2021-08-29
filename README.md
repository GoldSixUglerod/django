# djangoApi

### Start project
You need to use Python 3.8

Run commands in your terminal:
```bash
cp .env.example .env
```
Store model in project root directory (django) and name it 'model.zip' or set path to model in .env
```bash
pip install -r requirements.txt
docker-compose -f docker-compose.database.yml up -d
python src/manage.py runserver
```

![img.png](img.png)

![img_1.png](img_1.png)