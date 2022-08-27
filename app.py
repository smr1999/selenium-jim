from flask import Flask,render_template

app = Flask(__name__)

@app.route('/examples/<int:num>')
def examples(num):
    return render_template(f'examples/{num}/index.html')
    