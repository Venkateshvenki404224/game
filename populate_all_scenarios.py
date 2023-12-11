from pymongo import MongoClient

# Connect to MongoDB - update the connection string as necessary
client = MongoClient('mongodb://harry_potter:Qwertyuiop%40123@mongodb.selfmade.ninja:27017/?authSource=users')
db = client['harry_potter_wizard_game']
collection = db['stories']

# Stories Data with transitions
stories = [
    {
    "title": "The Enigmatic Potion",
    "content": {
        "introduction": "In the ancient alchemy lab, you discover a potion with shifting colors and no label. Its purpose is a mystery.",
        "choices": {
            "drink_potion": {"next_story": "Mystical Transformation", "description": "Risk drinking the potion, seeking its unknown effects."},
            "analyze_potion": {"next_story": "Scientific Discovery", "description": "Take the potion to the lab for analysis, uncovering its secrets scientifically."}
        }
    }
},
{
    "title": "The Whispering Woods",
    "content": {
        "introduction": "You find yourself lost in the Whispering Woods where the trees seem to speak, guiding you to an unknown path.",
        "choices": {
            "follow_voices": {"next_story": "Hidden Grove", "description": "Follow the voices, trusting the mysterious guidance."},
            "ignore_voices": {"next_story": "Lone Wanderer", "description": "Ignore the voices and find your own way out."}
        }
    }
},
{
    "title": "The Ancient Library",
    "content": {
        "introduction": "You enter a library with ancient, magical books. One book glows ominously, while another whispers your name.",
        "choices": {
            "read_glowing_book": {"next_story": "Cursed Knowledge", "description": "Read the glowing book, risking the curse for knowledge."},
            "read_whispering_book": {"next_story": "Secrets Revealed", "description": "Read the whispering book, uncovering personal secrets."}
        }
    }
},
{
    "title": "The Mysterious Traveler",
    "content": {
        "introduction": "A mysterious traveler offers you a choice between two enchanted items: a mirror that shows future possibilities or a key that opens any door.",
        "choices": {
            "choose_mirror": {"next_story": "Visions of the Future", "description": "Choose the mirror to see potential futures."},
            "choose_key": {"next_story": "Doors to the Unknown", "description": "Choose the key to unlock doors to unknown places."}
        }
    }
},
{
    "title": "The Starlit Summit",
    "content": {
        "introduction": "Atop a mountain under a starry sky, you find a celestial observatory pointing to either a distant nebula or a mysterious comet.",
        "choices": {
            "explore_nebula": {"next_story": "Galactic Journey", "description": "Adjust the observatory to explore the nebula."},
            "track_comet": {"next_story": "Comet's Secret", "description": "Use the observatory to track the comet's path."}
        }
    }
}
]

# Insert Stories into the Database
collection.insert_many(stories)

print("Stories successfully added to the database!")
