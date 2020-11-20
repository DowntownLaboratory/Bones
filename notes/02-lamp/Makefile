IMAGE_NAME=local/lamp

build:
	docker build -t ${IMAGE_NAME} .

run:
	docker run --privileged -it ${IMAGE_NAME}
	# https://stackoverflow.com/questions/30059784/docker-access-to-raspberry-pi-gpio-pins
	# docker run -it --device /dev/gpiomem ${IMAGE_NAME}
	# docker run -v /sys:/sys -it ${IMAGE_NAME}