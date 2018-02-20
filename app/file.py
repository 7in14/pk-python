from app import app

@app.route('/file')

def file():
    file_object = open('README.md', 'r')
    return file_object.read()
