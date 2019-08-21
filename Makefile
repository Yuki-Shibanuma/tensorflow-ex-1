d:
	docker run -it --rm -v $(PWD):/tmp -w /tmp tensorflow/tensorflow:latest-py3 python ./script.py
dd:
	docker run -it --rm -v $(PWD):/tmp -w /tmp tensor-keras python ./script.py
ddd:
	docker run -it --rm -v $(PWD):/tmp -w /tmp tensor-keras
build:
	docker build -t tensor-keras .