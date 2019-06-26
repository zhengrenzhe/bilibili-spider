get_docker_images:
	docker pull postgres:12
	docker pull rabbitmq:3.7.15
	docker pull redis:5.0.5
	docker pull sebp/elk:720


_create_postgres:
	mkdir -p ~/docker-data/postgres
	docker run --name postgres -e POSTGRES_PASSWORD=1234 -p 5432:5432 -v ~/docker-data/postgres:/var/lib/postgresql/data -d postgres:12


_create_redis:
	mkdir -p ~/docker-data/redis
	docker run -p 6379:6379 --name redis -v ~/docker-data/redis:/data -d redis:5.0.5 redis-server --appendonly yes


_create_rabbitmq:
	docker run -d --hostname rabbit --name rabbit -p 5672:5672 rabbitmq:3.7.15


_create_elk:
	docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -idt --name elk sebp/elk


create_containers: _create_postgres _create_rabbitmq _create_redis _create_elk
