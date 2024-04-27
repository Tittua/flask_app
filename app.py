import flask as Flask

app=Flask(__name__)

@app.route('/')
def home():
    return 'Hello Welcome to home page'


if __name__=='__main__':
    app.run()
