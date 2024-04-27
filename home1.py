from flask import Flask,redirect,url_for,render_template,request


app=Flask(__name__)


#decorator
@app.route('/')
def home():
    return render_template('index.html')
#variable rule
@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed '+ str(score)

#variable rule
@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed '+ str(score)

@app.route('/result/<int:marks>')
def result(marks):
    result=''
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))





if __name__=='__main__':
    app.run(debug=True)
