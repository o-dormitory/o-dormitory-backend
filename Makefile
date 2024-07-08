run:
	docker-compose up -d --build

stop:
	docker-compose down

makemigrations:
	docker-compose exec api python3 manage.py makemigrations

migrate:
	docker-compose exec api python3 manage.py migrate

test:
	docker-compose exec api python3 manage.py test