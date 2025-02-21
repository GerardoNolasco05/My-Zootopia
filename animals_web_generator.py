import json

def load_data(file_path):
    """Loads JSON file"""
    with open(file_path, 'r') as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()


def animal_content(animals_data):
    output = ''
    for animal_data in animals_data:
        output += '<li class="cards__item">'
        output += f"Name: {animal_data['name']}<br/>\n"
        output += f"Diet: {animal_data['characteristics']['diet']}<br/>\n"
        output += f"Location: {animal_data['locations'][0]}<br/>\n"
        if 'type' in animal_data['characteristics']:
            output += f"Type: {animal_data['characteristics']['type']}<br/>\n"
        output += '</li>\n'

    return output


# Replace the placeholder with the actual animal content
animal_info_html = animal_content(animals_data)
html_template = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_info_html)

# Save the modified HTML to a new file
with open("animals.html", "w", encoding="utf-8") as output_file:
    output_file.write(html_template)