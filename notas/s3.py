'''
aws_access_key_id=
aws_secret_access_key=
'''

from flask import Flask, request
import boto3

app = Flask(__name__)

@app.route('/')
def index():
    return '''<form method=POST enctype=multipart/form-data action="upload">
    <input type=file name=myfile>
    <input type=submit>
    </form>'''

@app.route('/upload')
def upload():
    s3 = boto3.resource('s3')

    s3.Bucket('prettyprinted').put_object(key='a_python_file.py',Body=request.files['myfile'])

    return '<h1>File saved to S3<\h1>'


if __name__ == '__main__':
    app.run(debug=True)