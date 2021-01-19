# project
Name heptas comes from the movie "Arrival", 2016. 
# Install
## Local 
For local development, we use venv. Python version 3.7.3.
```
source /path/to/virtualenv/python3.7/bin/activate
pip install -r requirements.txt
```
Install tesseract for image translation
- On ubuntu
```
sudo apt install tesseract
sudo apt install tesseract-ocr-[lang]
```
- On mac
```
brew install tesseract
sudo apt install tesseart-lang
```

Planning dockerized version when needed.


## Prod
* Install docker engine on your production host system. Use ubuntu here as example.
* build docker image. 
```
docker build -t heptas ./docker
docker images
```
run docker images to get a list of images in the system, you should see the images just built: heptas:latest

* start the container in daemon mode to keep container alive 
```
docker-compose -f docker/docker-compose.yml up -d
```
create a .env file in heptas/ dir. It (will) contains credentials so we do not commit it to github.
to turn down the service:
```
docker-compose -f docker/docker-compose.yml down
```

* exec the container to run the command inside.
```
docker ps
docker exec -it $(docker ps |grep heptas|awk '{print $1}') zsh
```
run docker ps to make sure you have the docker container running.

We should manually copy the data directories and files, as they are not committed to github.

We can edit codes in preferred editor, then run the command inside docker container.

# Run
For now, translation and reporting run with pytest scripts in tests.

## NLP Model Training
This part is currently in another repo, will be rewritten.

## Translation
```
cd test
pytest -s docx_processor.py
```

## Reporting
This requires translation process first, otherwise it will report failure.
```
cd test
pytest -s project_reporting.py
```
