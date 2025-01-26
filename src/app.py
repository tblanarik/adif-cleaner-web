from flask import Flask, render_template, request
import cleaner
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def parse_datetime(datetime_str):
    try:
        return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
    except ValueError:
        return None

def get_file_size(file):
    file.seek(0, 2)  # Move the cursor to the end of the file
    file_length = file.tell()
    file.seek(0)  # Move the cursor back to the start of the file
    return file_length

def read_and_filter_file_content(file, start_datetime, end_datetime, dedup):
    file_content = file.read().decode('utf-8').splitlines()
    file_content = cleaner.filter_adi_data(file_content, start_datetime, end_datetime, dedup)
    return '\n'.join(file_content)

@app.route('/index', methods=['GET', 'POST'])
def index():
    file_content = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        if get_file_size(file) > 1 * 1024 * 1024:  # 1MB
            return 'File is too large. Maximum size allowed is 1MB.'

        start_datetime_str = request.form.get('start_datetime')
        end_datetime_str = request.form.get('end_datetime')
        dedup = 'dedup' in request.form

        start_datetime = parse_datetime(start_datetime_str)
        if not start_datetime:
            return 'Invalid start datetime format'
        
        end_datetime = parse_datetime(end_datetime_str) if end_datetime_str else None
        if end_datetime_str and not end_datetime:
            return 'Invalid end datetime format'

        file_content = read_and_filter_file_content(file, start_datetime, end_datetime, dedup)
    
    return render_template('index.html', file_content=file_content)

if __name__ == '__main__':
    app.run(debug=True)