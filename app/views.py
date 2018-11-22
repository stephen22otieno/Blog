from flask import render_template
from app import app

@app.route('/Blog/<int:Blog_id>')
def Blog(Blog_id):

    '''
    View Blog page function that returns the Blog details page and its data
    '''
    return render_template('Blog.html',id = Blog_id)
