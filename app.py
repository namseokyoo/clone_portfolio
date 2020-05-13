from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def navbar():
    return render_template('portfolio.html')

if __name__=="__main__":
    app.run(host='localhost', port=5001, debug='True')  