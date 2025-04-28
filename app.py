from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            return "Video downloaded successfully!"
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
