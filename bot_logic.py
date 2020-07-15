def get_profiles():
    with open('profiles.txt') as f:
        text = f.readlines()
        text = [row.replace('\n', '') for row in text]
    return text
