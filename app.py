from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route('/')
def home():
  prompts = story.prompts
  return render_template('home.html', prompts=prompts)

@app.route('/story')
def the_story():
  text = story.generate(request.args)
  return render_template('story.html', text=text)