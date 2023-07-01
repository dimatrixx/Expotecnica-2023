from flask import Flask,render_template

app = Flask("Server-servo")

@app.route("/")
def unacoma_mesepara():
    return render_template("index.html")

@app.route("/ejemplonms")
def ejemplonms_route():
    return "Esto deberia de funcionar tipo omg like wtf"

if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0', port='5000')