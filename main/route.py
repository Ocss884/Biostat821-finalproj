import os
from main import app, db
from flask import render_template, send_from_directory

allocation = db.Table('jassen_allocation',db.metadata, autoload=True, autoload_with=db.engine)

@app.route('/')
@app.route('/map')
def map_page():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                                            'favicon.ico')

@app.route('/table')
def table_page():
    entry = db.session.query(allocation).all()
    return render_template('table.html',items=entry)