from flask import Flask, render_template, request
import cleaner
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/index', methods=['GET', 'POST'])
def index():
    file_content = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        # Check file size
        file.seek(0, 2)  # Move the cursor to the end of the file
        file_length = file.tell()
        file.seek(0)  # Move the cursor back to the start of the file
        if file_length > 1 * 1024 * 1024:  # 1MB
            return 'File is too large. Maximum size allowed is 1MB.'

        start_datetime_str = request.form.get('start_datetime')
        end_datetime_str = request.form.get('end_datetime')
        dedup = 'dedup' in request.form

        try:
            start_datetime = datetime.strptime(start_datetime_str, '%Y%m%dT%H%M%S')
        except ValueError:
            return 'Invalid start datetime format'
        
        end_datetime = None
        if end_datetime_str:
            try:
                end_datetime = datetime.strptime(end_datetime_str, '%Y%m%dT%H%M%S')
            except ValueError:
                return 'Invalid end datetime format'

        file_content = file.read().decode('utf-8').splitlines()
        file_content = cleaner.filter_adi_data(file_content, start_datetime, end_datetime, dedup)
        file_content = '\n'.join(file_content)
    
    return render_template('index.html', file_content=file_content)

if __name__ == '__main__':
    app.run(debug=True)