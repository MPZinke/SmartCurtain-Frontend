

all:
	docker build -t smartcurtain:frontend ./Source


run:
	set -a; source .env; set +a && docker run \
		-p 80:80 \
		-e SMARTCURTAIN_BACKEND_DOMAIN="$${SMARTCURTAIN_BACKEND_DOMAIN}" \
		smartcurtain:frontend


clean:
	docker rmi `docker images --filter dangling=true -q` --force


kill:
	docker stop `docker ps -q`
