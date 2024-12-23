from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Blog verilerini saklamak için
blogs = []

@app.route('/')
def index():
    return render_template('index.html', blogs=blogs)

@app.route('/add', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Resim yükleme
        image = request.files['image']
        image_path = None
        if image:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)
            image_path = image_path.replace('static/', '')

        # Blog ekleme
        blogs.append({'title': title, 'content': content, 'date': date, 'image': image_path})
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    # Flask uygulaması 5000 portunda çalışacak
    app.run(host='0.0.0.0', port=5000, debug=True)
