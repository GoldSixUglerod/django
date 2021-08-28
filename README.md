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
pip install poetry
poetry install
docker-compose -f docker-compose.database.yml up -d
```

Store model in root directory. (in djangoApi)