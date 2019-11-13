Host configuration:
-------------------------
- Python 3.7.0
- Virtualenv properly set-up with the LATEST version of setuptools and pip.
You can find more info about python packages and virtualenv here:
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
- Just clone and go into the project and run ```python3 setup.py install```


Latest chromedriver version (2.33 used):
```
https://chromedriver.storage.googleapis.com/index.html
```
*! chromedriver binary MUST be located in SYSTEM PATH*

Latest Selenium Standalone server:
```
https://www.seleniumhq.org/download/
```

Run tests:
```
pytest ~/weather/backend2/backend_test.py
```
Step-by-step installation on localhost:
```
$ cd /tmp
$ git clone https://github.com/lonely-caat/stuff.git
$ cd stuff/weather
$ virtualenv --python=python3.7 venv/
$ source venv/bin/activate
(venv)$ pip install -U pip setuptools
(venv)$ python3 setup.py install
(venv)$ pytest backend2/backend_test.py
! for the ui tests for now just run 
python3 frontend/test_frontend.py
```
