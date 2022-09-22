# Python-Test-Project
Using Flask to build a Web Application for User.
Integration with Flask, Flask-SQLalchemy,and Flask-Login.

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Application Structure 
```
.
|──────static
| |────styles.css
|──────templates
| |────layout.html
| |────login.html
| |────signup.html
| |────user.html
|──────app.py
|──────requirments.txt

```

## Flask Configuration

#### Example

```
app = Flask(__name__)
app.config['DEBUG'] = True

```
```
##Flask settings
DEBUG = True  # True/False
....

```

## Run Flask
### Run flask for develop
```
$ python app.py
```

## Document page
```
In flask, Default port is `5000`

Budget document page:  `http://127.0.0.1:5000/login`
```
