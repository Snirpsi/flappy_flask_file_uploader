build-docker:
	docker build -t flappy_flask_file_uploader .

run-docker:
	docker run --rm -d -p 7777:7777 flappy_flask_file_uploader
