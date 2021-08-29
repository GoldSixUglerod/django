# djangoApi

### Start project
You need to use Docker and Python 3.8

If you use Linux or MacOs, then run command (if you use Windows, then rename .env.example to .env):
```bash
cp .env.example .env
```
Download model (http://vectors.nlpl.eu/repository/20/185.zip), store it in project root directory (django), and name it 'model.zip' or set path to model in .env

Run commands in your terminal:
```bash
pip install -r requirements.txt
docker-compose -f docker-compose.database.yml up -d
python src/manage.py runserver
```

![img.png](img.png)

![img_1.png](img_1.png)