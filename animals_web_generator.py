import json


def load_data(file_path):
    """Load JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_animal_data():
    """Load the animals_template.html file and return its content."""
    with open("animals_template.html", "r", encoding="utf-8") as file:
        return file.read()


def animal_content(animals_data):
    """Generate HTML list items for animals."""
    output = []

    for animal in animals_data:
        output.append(f'''
        <li class="cards__item">
            <div class="card__title">{animal["name"]}</div>
            <p class="card__text">
                <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>
                <strong>Location:</strong> {animal["locations"][0]}<br/>
                {(
                    f'<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>'
                    if "type" in animal["characteristics"]
                    else ""
                )}
            </p>
        </li>
        ''')

    return "\n".join(output)


def generate_animal_html(template, animals_data):
    """Insert animal data into the HTML template."""
    animal_info_html = animal_content(animals_data)
    return template.replace("__REPLACE_ANIMALS_INFO__", animal_info_html)


def save_html(filename, content):
    """Save the given content to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    """Main function to process animal data and generate an HTML file."""
    animals_data = load_data("animals_data.json")
    html_template = load_animal_data()
    updated_html = generate_animal_html(html_template, animals_data)
    save_html("animals.html", updated_html)
    print("HTML file generated successfully: animals.html")


if __name__ == "__main__":
    main()
