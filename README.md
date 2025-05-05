# FastAPI Containerized Application

This is a containerized FastAPI application with PostgreSQL, Redis, and Nginx using Docker Compose.

## Features

- FastAPI web application
- PostgreSQL database
- Redis cache
- Nginx reverse proxy
- Multi-stage Docker builds for optimization

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Build and start the containers:
```bash
docker-compose up --build
```

3. Access the application:
- Main application: http://localhost
- API documentation: http://localhost/docs
- Health check: http://localhost/health
- Test check redis: http://localhost/test/redis
- Test check postgreSql: http://localhost/test/postgres

## Project Structure

```
.
├── app/
│   └── main.py
├── nginx/
│   └── nginx.conf
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Environment Variables

The following environment variables are used in the application:

- `REDIS_HOST`: Redis host (default: redis)
- `REDIS_PORT`: Redis port (default: 6379)
- `DATABASE_URL`: PostgreSQL connection URL
- `POSTGRES_USER`: PostgreSQL username
- `POSTGRES_PASSWORD`: PostgreSQL password
- `POSTGRES_DB`: PostgreSQL database name

## Refrences
- `dockerfile fastapi`: https://medium.com/@alidu143/containerizing-fastapi-app-with-docker-a-comprehensive-guide-416521b2457c
- `fastapi deployement`: https://fastapi.tiangolo.com/deployment/docker/#recap
- `nginx configuration`: https://www.plesk.com/blog/various/nginx-configuration-guide/

## Development

To run the application in development mode:

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

## License

MIT 