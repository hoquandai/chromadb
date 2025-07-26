run-chroma:
	docker compose -f docker/docker-compose.yml up chromadb

run-app:
	docker compose -f docker/docker-compose.yml run --rm app
