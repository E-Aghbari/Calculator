from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    number = request.form.get('number')
    
    return render_template('index.html', number=number)


def calculate():
    pass

if __name__ == '__main__':
    app.run(debug = True)