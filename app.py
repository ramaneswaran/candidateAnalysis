from flask import Flask, render_template, request
import analyse 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    analyse.analyse_candidates()
    return render_template('index.html', candidates = analyse.candidates)

if __name__ == '__main__':
    app.run(debug=True)