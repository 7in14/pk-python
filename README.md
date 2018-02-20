# About [![Build Status](https://travis-ci.org/7in14/pk-python.svg?branch=master)](https://travis-ci.org/7in14/pk-python
[![Maintainability](https://api.codeclimate.com/v1/badges/26029d757952f052d146/maintainability)](https://codeclimate.com/github/7in14/pk-python/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/26029d757952f052d146/test_coverage)](https://codeclimate.com/github/7in14/pk-python/test_coverage)
Simple python web app built with flask

## To run with flask
Export app name first
```
$ export FLASK_APP=hello.py
```
## To run with Python
```
python hello.py
```
That's to this code in `hello.py`
```
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
```


## Virtual environments
To create a python virtual environment

### Get virtualenv package
```
$ sudo pip install virtualenv
```
If pip is missing on OSX you get this `easy_install`
```
$ easy_install pip
```

### Create virtual environment
```
$ virtualenv venv
```

### Activate virtual environment
```
$ source venv/bin/activate
```

#### Installing new packages
```
$ pip install [package]
```

#### Restore packages
