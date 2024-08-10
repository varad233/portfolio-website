from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/certificates')
def certificates():
    return render_template('certificates.html')

@app.route('/club_activities')
def club_activities():
    return render_template('club_activities.html')

if __name__ == '__main__':
    app.run(debug=True)
