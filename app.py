from flask import Flask

app = Flask(__name__)

@app.route('/<letter>')  
def parameter(letter):         
    return '%s flask world' %letter


print(__name__)
if __name__ == "__main__":
    print("shit")
    app.run(host='0.0.0.0')
