def add_synonyms(statement):
    synonyms = [
        {
            "baseWord" : "E. Zarate Hospital",
            "synonyms" : ["Zarate", "E. Zarate", "Zarate Hospital", "Hospital"]
        }
    ]
    for synonym in synonyms:
        for word in synonym['synonyms']:
            if word in statement.text:
                statement.text = statement.text.replace(word, synonym['baseWord'])
                break
    return statement

def correct_zarate(statement):
    """
        Converts all variations of Zarate Hospital to E. Zarate Hospital
    """
    import re
    pattern = r'\b\w*Zarate\w*\b'
    matches = re.finditer(pattern, statement.text)
    for match in matches:
        statement.text = statement.text.replace(match.group(0), "E. Zarate Hospital")
    return statement

def correct_location(statement):
    """
        Converts all variations of location to address
    """
    import re
    pattern = r'\b\w*location\w*\b'
    matches = re.finditer(pattern, statement.text)
    for match in matches:
        statement.text = statement.text.replace(match.group(0), "address")
    return statement