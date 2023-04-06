from flask import Flask, render_template
from datetime import datetime
from requests import *
from random import *

app = Flask(__name__)
num = randint(1, 100)


@app.route('/')
def home():
    year = datetime.now().strftime('%Y')
    return render_template('index.html', year=year, num=num)


@app.route('/guess/<name>')
def age_guess(name):
    gender_api = get(url=f"https://api.genderize.io/?name={name}")
    age_api = get(url=f"https://api.agify.io?name={name}")

    return render_template('age.html', name=name, gender=gender_api.json()["gender"], age=age_api.json()["age"])


@app.route("/blog/<int:num>")
def get_blog(num):
    print(num)
    blog_url = get(url=f"https://api.npoint.io/2410f32edd5fd309369c")
    all_posts = blog_url.json()
    return render_template('blog.html', posts=all_posts)
        

if __name__ == "__main__":
    app.run(debug=True)
