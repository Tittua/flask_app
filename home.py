from flask import Flask,redirect,url_for,request,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result/<int:score>')
def result(score):
    if score<50:
        res='fail'
    else:
        res='pass'
    return render_template('result.html',result=res)


@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        phy=float(request.form['physics'])
        total_score=(science+maths+phy)/3
        

    return redirect(url_for('result',score=total_score))








if __name__=='__main__':
    app.run(debug=True)
