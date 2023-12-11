from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
# import os

application = app = Flask(__name__)

# MongoDB connection
# mongo_uri = os.environ.get('MONGO_URI')
# if not mongo_uri:
#     raise ValueError("No MONGO_URI set for Flask application")

client = MongoClient("mongodb://harry_potter:Qwertyuiop%40123@mongodb.selfmade.ninja:27017/?authSource=users")
db = client['harry_potter_wizard_game']
collection = db['stories']

@app.route('/', methods=['GET', 'POST'])
def index():
    story_title = "The Hidden Room"  # Starting story
    if request.method == 'POST':
        user_choice = request.form['choice']
        next_story = collection.find_one({"title": user_choice})
        if next_story:
            story_title = next_story['title']
        else:
            story_title = "End" 
            return render_template('end.html') # End of story sequence

    story = collection.find_one({"title": story_title})
    return render_template('index.html', story=story)

if __name__ == '__main__':
    app.run(debug=False)
