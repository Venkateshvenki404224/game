
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
db = SQLAlchemy(app)

class Scenario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    option_a = db.Column(db.String, nullable=False)
    option_b = db.Column(db.String, nullable=False)
    next_a = db.Column(db.String, nullable=True)
    next_b = db.Column(db.String, nullable=True)

@app.route('/')
def index():
    scenario = Scenario.query.get(1)  # Start with the first scenario
    return render_template('index.html', scenario=scenario)

@app.route('/<int:scenario_id>', methods=['POST'])
def choose_option(scenario_id):
    chosen_option = request.form.get('option')
    current_scenario = Scenario.query.get(scenario_id)
    
    if chosen_option == 'A':
        next_scenario_id = current_scenario.next_a
    else:
        next_scenario_id = current_scenario.next_b
    
    # Check if game is over
    if next_scenario_id == 'end':
        return render_template('end.html')
    
    next_scenario = Scenario.query.get(int(next_scenario_id))
    return render_template('index.html', scenario=next_scenario)

if __name__ == '__main__':
    app.run(debug=True)
