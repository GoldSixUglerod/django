# djangoApi

### Start project
```bash
cp .env.example .env
pip install -r requirements.txt
docker-compose -f docker-compose.database.yml up -d
python src/manage.py runserver
```

Store model in project root directory (django) and name it 'model.zip' or set path to model in .env