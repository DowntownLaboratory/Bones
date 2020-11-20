IMAGE_NAME=local/blink

build:
	docker build -t ${IMAGE_NAME} .

run:
	docker run -d --device /dev/gpiomem ${IMAGE_NAME}