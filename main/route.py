import os
from main import app, db
from flask import render_template, send_from_directory

pfizer = db.Table('Pfizer_allocation',db.metadata, autoload=True, autoload_with=db.engine)
moderna = db.Table('Moderna_allocation',db.metadata, autoload=True, autoload_with=db.engine)

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
    entry = db.session.query(pfizer).all()
    return render_template('table.html',items=entry)

@app.route('/table2')
def table2_page():
    entry = db.session.query(moderna).all()
    return render_template('table2.html',items=entry)