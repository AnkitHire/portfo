import csv

from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/')
def my_main():
    return render_template('index.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        info = data["info"]
        file = database.write(f'\n{email},{subject},{info}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        info = data["info"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, info])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'try again'
