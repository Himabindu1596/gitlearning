from flask import Flask
app = Flask(__name__)
@app.route('/')
def Hello():
    return "welcome"
@app.route('/welcome/<name>')
def Welcome(name):
    return f"Welcome {name}"
@app.route('/welcome/<num>')
def welcomenum(num):
    return f"welcome {num}"
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8800)
