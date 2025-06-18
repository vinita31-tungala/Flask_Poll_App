from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Poll question and options
question = "What is your favorite programming language?"
options = ["Python", "JavaScript", "Java", "C++"]

# Votes stored in a dictionary, initially zero for all options
votes = {option: 0 for option in options}

@app.route('/')
def index():
    return render_template('index.html', question=question, options=options)

@app.route('/vote', methods=['POST'])
def vote():
    selected_option = request.form.get('option')
    if selected_option in votes:
        votes[selected_option] += 1
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('results.html', question=question, votes=votes)

if __name__ == '__main__':
    app.run(debug=True)
