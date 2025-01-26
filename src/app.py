from flask import Flask, render_template, request

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
        file_content = file.read().decode('utf-8')
    return render_template('index.html', file_content=file_content)

if __name__ == '__main__':
    app.run(debug=True)