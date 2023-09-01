
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
db = SQLAlchemy(app)

db.create_all()

class Scenario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    option_a = db.Column(db.String, nullable=False)
    option_b = db.Column(db.String, nullable=False)
    next_a = db.Column(db.String, nullable=True)
    next_b = db.Column(db.String, nullable=True)


# Adding all scenarios to the database
new_scenario = Scenario(
    id=1,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=2,
    next_b=3
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=2,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=4,
    next_b=3
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=3,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=5,
    next_b=5
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=4,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=5,
    next_b=5
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=5,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=6,
    next_b=7
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=6,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=8,
    next_b=7
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=7,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=9,
    next_b=10
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=8,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=11,
    next_b=12
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=9,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=13,
    next_b=14
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=10,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=15,
    next_b=16
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=11,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=12,
    next_b=12
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=12,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=13,
    next_b=13
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=13,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=14,
    next_b=14
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=14,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=15,
    next_b=15
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=15,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=16,
    next_b=16
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=16,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=17,
    next_b=17
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=17,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=18,
    next_b=18
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=18,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=19,
    next_b=19
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=19,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=20,
    next_b=20
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=20,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=21,
    next_b=21
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=21,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=22,
    next_b=22
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=22,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=23,
    next_b=23
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=23,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=24,
    next_b=24
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=24,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=25,
    next_b=25
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=25,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=26,
    next_b=26
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=26,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=27,
    next_b=27
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=27,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=28,
    next_b=28
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=28,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=29,
    next_b=29
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=29,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=30,
    next_b=30
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=30,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=31,
    next_b=31
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=31,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=32,
    next_b=32
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=32,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=33,
    next_b=33
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=33,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=34,
    next_b=34
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=34,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=35,
    next_b=35
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=35,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=36,
    next_b=36
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=36,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=37,
    next_b=37
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=37,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=38,
    next_b=38
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=38,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=39,
    next_b=39
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=39,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=40,
    next_b=40
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=40,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=41,
    next_b=41
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=41,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=42,
    next_b=42
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=42,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=43,
    next_b=43
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=43,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=44,
    next_b=44
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=44,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=45,
    next_b=45
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=45,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=46,
    next_b=46
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=46,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=47,
    next_b=47
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=47,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=48,
    next_b=48
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=48,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=49,
    next_b=49
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=49,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=50,
    next_b=50
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=50,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=51,
    next_b=51
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=51,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=52,
    next_b=52
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=52,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=53,
    next_b=53
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=53,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=54,
    next_b=54
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=54,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=55,
    next_b=55
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=55,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=56,
    next_b=56
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=56,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=57,
    next_b=57
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=57,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=58,
    next_b=58
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=58,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=59,
    next_b=59
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=59,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=60,
    next_b=60
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=60,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=61,
    next_b=61
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=61,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=62,
    next_b=62
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=62,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=63,
    next_b=63
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=63,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=64,
    next_b=64
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=64,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=65,
    next_b=65
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=65,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=66,
    next_b=66
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=66,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=67,
    next_b=67
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=67,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=68,
    next_b=68
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=68,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=69,
    next_b=69
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=69,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=70,
    next_b=70
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=70,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=71,
    next_b=71
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=71,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=72,
    next_b=72
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=72,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=73,
    next_b=73
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=73,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=74,
    next_b=74
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=74,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=75,
    next_b=75
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=75,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=76,
    next_b=76
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=76,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=77,
    next_b=77
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=77,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=78,
    next_b=78
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=78,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=79,
    next_b=79
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=79,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=80,
    next_b=80
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=80,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=81,
    next_b=81
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=81,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=82,
    next_b=82
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=82,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=83,
    next_b=83
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=83,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=84,
    next_b=84
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=84,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=85,
    next_b=85
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=85,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=86,
    next_b=86
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=86,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=87,
    next_b=87
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=87,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=88,
    next_b=88
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=88,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=89,
    next_b=89
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=89,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=90,
    next_b=90
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=90,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=91,
    next_b=91
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=91,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=92,
    next_b=92
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=92,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=93,
    next_b=93
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=93,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=94,
    next_b=94
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=94,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=95,
    next_b=95
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=95,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=96,
    next_b=96
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=96,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=97,
    next_b=97
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=97,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=98,
    next_b=98
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=98,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=99,
    next_b=99
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=99,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=100,
    next_b=100
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=100,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=101,
    next_b=101
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=101,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=102,
    next_b=102
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=102,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=103,
    next_b=103
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=103,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=104,
    next_b=104
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=104,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=105,
    next_b=105
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=105,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=106,
    next_b=106
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=106,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=107,
    next_b=107
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=107,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=108,
    next_b=108
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=108,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=109,
    next_b=109
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=109,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=110,
    next_b=110
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=110,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=111,
    next_b=111
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=111,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=112,
    next_b=112
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=112,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=113,
    next_b=113
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=113,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=114,
    next_b=114
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=114,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=115,
    next_b=115
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=115,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=116,
    next_b=116
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=116,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=117,
    next_b=117
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=117,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=118,
    next_b=118
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=118,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=119,
    next_b=119
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=119,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=120,
    next_b=120
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=120,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=121,
    next_b=121
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=121,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=122,
    next_b=122
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=122,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=123,
    next_b=123
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=123,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=124,
    next_b=124
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=124,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=125,
    next_b=125
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=125,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=126,
    next_b=126
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=126,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=127,
    next_b=127
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=127,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=128,
    next_b=128
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=128,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=129,
    next_b=129
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=129,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=130,
    next_b=130
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=130,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=131,
    next_b=131
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=131,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=132,
    next_b=132
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=132,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=133,
    next_b=133
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=133,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=134,
    next_b=134
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=134,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=135,
    next_b=135
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=135,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=136,
    next_b=136
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=136,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=137,
    next_b=137
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=137,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=138,
    next_b=138
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=138,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=139,
    next_b=139
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=139,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=140,
    next_b=140
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=140,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=141,
    next_b=141
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=141,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=142,
    next_b=142
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=142,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=143,
    next_b=143
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=143,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=144,
    next_b=144
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=144,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=145,
    next_b=145
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=145,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=146,
    next_b=146
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=146,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=147,
    next_b=147
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=147,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=148,
    next_b=148
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=148,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=149,
    next_b=149
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=149,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a=150,
    next_b=150
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=150,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a=151,
    next_b=151
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=151,
    text='You\'ve been tipped off about a high-security vault in the city\'s main bank. How do you proceed?',
    option_a='Gather a team to plan an intricate heist.',
    option_b='Use a mole inside the bank to get more details.',
    next_a=152,
    next_b=152
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=152,
    text='A team member suggests tunneling under the bank as the main entry point. What\'s your decision?',
    option_a='Agree, but ensure you have an expert on the team.',
    option_b='Consider a more direct approach to avoid long-term exposure.',
    next_a=153,
    next_b=153
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=153,
    text='The bank has recently updated its security system. How do you adapt?',
    option_a='Hack into the security company\'s system to learn about the updates.',
    option_b='Bribe a bank employee for insider information.',
    next_a=154,
    next_b=154
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=154,
    text='A former associate offers insider information in exchange for a cut. Do you agree?',
    option_a='Accept the offer but stay cautious.',
    option_b='Decline and rely on your own sources.',
    next_a=155,
    next_b=155
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=155,
    text='Security is tighter during the day. When do you plan the heist?',
    option_a='Opt for a night operation.',
    option_b='Create a diversion during the day and proceed.',
    next_a=156,
    next_b=156
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=156,
    text='A team member has been acting suspicious lately. What\'s your move?',
    option_a='Confront them privately.',
    option_b='Keep an eye on them discreetly.',
    next_a=157,
    next_b=157
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=157,
    text='The police have received a tip about your plan. How do you react?',
    option_a='Change the plan entirely.',
    option_b='Feed them false information to mislead them.',
    next_a=158,
    next_b=158
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=158,
    text='A notorious gang offers assistance. Do you collaborate?',
    option_a='Join forces but remain wary.',
    option_b='Politely decline, avoiding potential double-crossing.',
    next_a=159,
    next_b=159
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=159,
    text='You find out there\'s a gala event at the bank. How do you use this to your advantage?',
    option_a='Blend in with the guests and recon.',
    option_b='Delay the heist to avoid extra witnesses.',
    next_a='end',
    next_b='end'
)
db.session.add(new_scenario)

new_scenario = Scenario(
    id=160,
    text='The getaway driver suggests using motorcycles instead of a van. Your thoughts?',
    option_a='Agree, valuing speed over capacity.',
    option_b='Stick to the van for its inconspicuous nature.',
    next_a='end',
    next_b='end'
)
db.session.add(new_scenario)

db.session.commit()