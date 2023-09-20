### Integrate HTML with Flask
### HTTP verbs .. GET, POST, etc
###jinja2 template engine
'''
{{.....}}       some expression value/s
{%.......%}     for statements, conditions
{#......#}      comments
'''

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome my friend WELCOME!"
#    return render_template('index.html',message="Welcome my friend WELCOME!")

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/success/<int:score>")
def success(score):
#    return "The person has PASSED with score "+ str(score)
    return render_template('result1.html',result=score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person has FAILED with score "+ str(score)

###Result checker
@app.route("/results/<int:marks>")
def results(marks):
    result=''
    if marks<50:
        result = 'fail'
    else:
        result = 'success'

    return redirect(url_for(result,score=marks))

###Result checker submit rechecker page
@app.route("/submit",methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4

    return redirect(url_for('results',marks=total_score))

if __name__ == '__main__':
    app.run(debug=True)