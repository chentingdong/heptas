# project
Name heptas comes from the movie "Arrival", 2016. 
# Install
For local development, we use venv. Python version 3.7.3.
```
source /path/to/virtualenv/python3.7/bin/activate
pip install -r requirements.txt
```
## install tesseract for image translation
On ubuntu
```
sudo apt install tesseract
sudo apt install tesseract-ocr-[lang]
```
On mac
```
brew install tesseract
sudo apt install tesseart-lang
```

Planning dockerized version when needed.
# Run
translation and reporting run with test scripts.

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
