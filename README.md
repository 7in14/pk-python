# About
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
