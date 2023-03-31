from models import *
from flask import Flask,request,render_template

@app.route('/')
def app_landing_page():
    return render_template('index.html')

@app.route('/register',methods = ['GET','POST'])
def register_here():
    message = ''
    if request.method == 'POST':
        formdata = request.form
        userrecord = Person(firstname=formdata.get('fname'),
             email=formdata.get('email'),
             lastname=formdata.get('lname'),
            phone=formdata.get('lname'),
             gender=formdata.get('gender'))
        db.session.add(userrecord)
        db.session.commit()
        message = "User Added Successfully...!"
    return render_template('register.html',message = message)


if __name__ == '__main__':
    app.run(debug=True)