FROM tensorflow/tensorflow:latest-py3
RUN pip install --upgrade pip
RUN pip install tensorflow==2.0.0-beta0
RUN pip install -U keras==2.0
RUN pip install -q matplotlib pillow scipy
RUN pip install -q -U tensorflow_hub