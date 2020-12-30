FROM python:3.8

RUN apt update
RUN apt install -y vim zsh net-tools software-properties-common

RUN add-apt-repository universe

RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
RUN mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
RUN add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
RUN apt update
RUN apt install cuda

COPY requirements.txt /app
RUN pip install OpenNMT-py OpenNMT-tf

WORKDIR /app
