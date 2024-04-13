import sys
sys.path.append('controller')
from flask import Flask, redirect, render_template, request, url_for
from signin import signin_controller

app = Flask(__name__)

@app.route('/')
def dashboard(name=None,uname=None):
    return render_template('dashboard.html')

@app.route('/signin',methods=['GET','POST'])
def signin():
    error = None
    if request.method == 'POST':
        # if request.form['uname'] != 'admin' or request.form['password'] != 'admin':
        #     error = 'Invalid Credentials. Please try again.'
        # else:
        #     return redirect(url_for('dashboard'))
        # name = request.form['name']
        # uname = request.form['uname']
        formData = {}
        for field in request.form:
            formData[field] = (request.form[field])
        response = signin_controller(formData)
        if(response != 'inserted'):
            return render_template('signin.html', error=response)
        return render_template('dashboard.html',response = response )
    return render_template('signin.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)