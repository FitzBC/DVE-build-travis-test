from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    with open('1.txt') as f:
        content=f.read()
    return content

@app.route("/config", methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        content=request.form.get('file_content')
        with open('1.txt','w') as f:
            f.write(content)
        return "Config success!"
    else:
        return "Need post file_content parameter!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)