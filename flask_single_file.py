from flask import Flask, request

app = Flask(__name__)

def main(basic_input='test'):
    # do whatever you want here
    return 'returned from main: {0}'.format(basic_input)

@app.route("/", methods=['GET', 'POST'])
def run_script():
    if request.form:
        output = main(request.form['basic_input'])
    else:
        output = ''

    return """
        Enter Your Input:</br>
        <form method="POST">
            <input name="basic_input">
            <input type="submit" value="Submit">
        </form></br>
        Output:</br>
        """ + output

if __name__ == "__main__":
    app.run(debug=True)
