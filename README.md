# djangoApi

### Start project
To start backend for frontend:
```bash
mv .env.example
docker-compose -f docker-compose.server.yml up -d
```

For local development:
```bash
cp .env.example .env
pip install -r requirements.txt
docker-compose -f docker-compose.database.yml up -d
```

Store model in project root directory and name it 'model.zip'. (in django)