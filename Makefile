build:
	docker compose -f docker.yml up --build -d --remove-orphans

up:
	docker compose -f docker.yml up -d

down:
	docker compose -f docker.yml down

show-logs:
	docker compose -f docker.yml logs

show-logs-api:
	docker compose -f docker.yml logs api

makemigrations:
	docker compose -f docker.yml run --rm api python manage.py makemigrations

migrate:
	docker compose -f docker.yml run --rm api python manage.py migrate

collectstatic:
	docker compose -f docker.yml run --rm api python manage.py collectstatic --no-input --clear

superuser:
	docker compose -f docker.yml run --rm api python manage.py createsuperuser

down-v:
	docker compose -f docker.yml down -v

volume:
	docker volume inspect src_local_postgres_data

authors-db:
	docker compose -f docker.yml exec postgres psql --username=alphaogilo --dbname=authors-live

flake8:
	docker compose -f docker.yml exec api flake8 .

black-check:
	docker compose -f docker.yml exec api black --check --exclude=migrations .

black-diff:
	docker compose -f docker.yml exec api black --diff --exclude=migrations .

black:
	docker compose -f docker.yml exec api black --exclude=migrations .

isort-check:
	docker compose -f docker.yml exec api isort . --check-only --skip venv --skip migrations

isort-diff:
	docker compose -f docker.yml exec api isort . --diff --skip venv --skip migrations

isort:
	docker compose -f docker.yml exec api isort . --skip venv --skip migrations


