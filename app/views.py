from flask import render_template
from app import app

@app.route('/Blog/<int:Blog_id>')
def Blog(Blog_id):

    '''
    View Blog page function that returns the Blog details page and its data
    '''
    title = 'Home - Welcome to The best Blog  Website Online'
    return render_template('index.html', title = title)
