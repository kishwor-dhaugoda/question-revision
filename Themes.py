import json

themes = {}

def load_themes():
    global themes

    with open('categories_themes.json', 'r') as file:
        data = json.load(file)    
        themes = data["themes"]    

def get_theme():
    global themes
    return themes["theme1"]

