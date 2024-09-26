
### **Installation **
```
git clone https://github.com/void20005/ftb_selenium.git
cd ftb_selenium
```
#### Create .env file with variables like:
```
APP_URL = 
APP_USERNAME=
APP_PASSWORD=
```
#### If you prefer to use venv:
```
python -m venv venv
source venv/bin/activate
```

#### Install requirements:
```
pip install -r requirements.txt
```
#### Collecting tests:
```
python -m pytest --co
```

#### Run specified test:
```
pytest -k <test_name>
```

#### Example:
```
pytest -k login_test.py
```
##### or if you use venv:
```
deactivate
source venv/bin/activate