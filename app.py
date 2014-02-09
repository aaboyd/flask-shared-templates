from flask import Flask
from flask import render_template
from jinja2 import ChoiceLoader, FileSystemLoader
import os

app = Flask(__name__)

base_dir = os.path.dirname(os.path.realpath(__file__))

app.jinja_loader = ChoiceLoader([FileSystemLoader(os.path.join(base_dir, 'templates')),
                                 FileSystemLoader(os.path.join(base_dir, 'static', 'templates'))]);

@app.route('/')
def hello_world():
    items = [{
        'title': 'Facebook',
        'body': 'Facebook is a social utility that connects people with friends and others who work, study and live around them.'
    }, {
        'title': 'Twitter',
        'body': 'Twitter is an online social networking and microblogging service that enables users to send and read "tweets", which are text messages limited to 140 characters.'
    }, {
        'title': 'LinkedIn',
        'body': 'LinkedIn is a social networking website for people in professional occupations.'
    }];
    return render_template('index.html', items=items )

if __name__ == '__main__':
    app.run(debug=True)