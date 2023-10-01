import spacy
from spacy.matcher import PhraseMatcher

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Create a PhraseMatcher object
matcher = PhraseMatcher(nlp.vocab)

# Define a list of phrases you want to match
phrases = ["New York City", "Los Angeles", "San Francisco"]

# Convert the phrases into Doc objects
phrase_patterns = [nlp(phrase) for phrase in phrases]

# Add the patterns to the PhraseMatcher
matcher.add("CityMatcher", None, *phrase_patterns) # type: ignore

# Input text
text = "I love New York City, and I want to visit San Francisco."

# Process the text with spaCy
doc = nlp(text)

# Find matches using the PhraseMatcher
matches = matcher(doc)

# Extract the matched phrases and their positions
for match_id, start, end in matches:
    matched_phrase = doc[start:end]
    print(f"Matched Phrase: {matched_phrase.text} (Start: {start}, End: {end})")
