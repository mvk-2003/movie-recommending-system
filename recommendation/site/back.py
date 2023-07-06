from flask import Flask, render_template,request
from main import out

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route('/submit', methods = ["POST","GET"])
def submit():
    if request.method == "POST" :
        result = request.form.to_dict()
        GENRES = request.form.getlist('GENRES')
        DIRECTOR = result['DIRECTOR']
        ACTORS = result['ACTORS']
        YEAR = result['YEAR']
        STUDIOS = result['STUDIOS']
        THEMES = result['THEMES']
        res = [GENRES,DIRECTOR,ACTORS,YEAR,STUDIOS,THEMES]
        outputs = out(res[0],res[1],res[2],res[3],res[4],res[5])
        return render_template("final.html",data = outputs)
    
if __name__ == '__main__':
    app.run(debug=True)
