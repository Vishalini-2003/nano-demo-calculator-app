from flask import Flask,request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    arr=request.json
    var1=arr['first']
    var2=arr['second']
    return {'result':var1+var2}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    arr=request.json
    var1=arr['first']
    var2=arr['second']
    return {'result':var1-var2}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
