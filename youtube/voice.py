import pyttsx3
import json

# Initialize the Text-to-speech engine
engine = pyttsx3.init()

# Set the voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Index 0 is for English-US voice
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)
# Load the JSON file
with open('article.json', 'r') as f: #article.json must be in same directory
    data = json.load(f)

# Get the title from the first object in the JSON file
title = data[0]['title']
# Get the content from the first object in the JSON file
content = data[0]['content']
# Combine title and content
final = title + "Proceeding to read story now." + content
# Convert text to speech & Save
engine.save_to_file(final, 'test.mp3')
engine.runAndWait()
