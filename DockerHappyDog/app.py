from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Little Sweet Puppy</title>
    </head>
    <body>
        <h1>Sevimli Köpek Yavrusu</h1>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXFFdaiATWvNh91lL2C6_xlmXUJ-25HfQWDg&s" alt="Köpek Yavrusu">
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
