from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        link = request.form['link']
        try:
            yt = YouTube(link)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            message = f"✅ Downloaded: {yt.title}"
        except Exception as e:
            message = f"❌ Error: {str(e)}"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
