FROM python:3.8-slim

RUN apt-get update \
  && apt-get install -y apt-utils wget ssh vim zsh git net-tools build-essential \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /root/.cache

# RUN apt-get install -y software-properties-common \
#   && add-apt-repository ppa:jonathonf/python-3.8 \
#   && apt-get update \
#   && apt-get install -y python3.8 \
#   && apt-get install -y python3-pip 
# RUN ln -s /usr/bin/python3.8 /usr/bin/python
RUN python -m pip install --upgrade pip

RUN mkdir /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY __init__.py /app

RUN sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
ENTRYPOINT ["/bin/bash"]

WORKDIR /app
