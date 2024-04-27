from flask import Flask

app=Flask(__name__)


#decorator
@app.route('/')
def home():
    return 'Hello Welcome to home page'

#variable rule
@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed '+ str(score)

#variable rule
@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed '+ str(score)


if __name__=='__main__':
    app.run(debug=True)
