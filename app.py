from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/welcome')
def app_welcome():
    return "Flask App is Running...!"

@app.route('/index')
def app_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)
