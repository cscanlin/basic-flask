from flask import render_template

from app import app
from app.forms import BasicForm
from app.my_script import main

@app.route("/", methods=['GET', 'POST'])
def run_script():
    form = BasicForm()
    if form.basic_input.data:
        output = main(form.basic_input.data)
    else:
        output = ''
    return render_template('index.html', output=output, form=form)
