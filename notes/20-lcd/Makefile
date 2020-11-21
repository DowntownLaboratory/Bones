IMAGE_NAME=local/gpio

build:
	docker build -t ${IMAGE_NAME} .

run:
	# https://stackoverflow.com/questions/30059784/docker-access-to-raspberry-pi-gpio-pins
	docker run --privileged -it ${IMAGE_NAME}
	# docker run -it --device /dev/gpiomem ${IMAGE_NAME}
	# docker run -v /sys:/sys -it ${IMAGE_NAME}

test:
	i2cdetect -y 1