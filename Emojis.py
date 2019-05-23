from emoji_data_python import emoji_short_names
import json

for code, emoji in emoji_short_names.items():
    name = emoji.short_name;
    if len(name) > 20:
        title = name[0:17] + "..."
    else:
        title = name
    folder = engine.get_folder("My Phrases")
    abbr = ":" + name + ":";
    engine.create_abbreviation(folder, title, abbr, emoji.char)
    time.sleep(0.1)
    # edit json data
    if title == "+1":
        title = "1"
    json_file_name = "/home/kevin/.config/autokey/data/My Phrases/." + title + ".json"
    with open(json_file_name, "r+") as file:
      data = json.load(file)
      data['sendMode'] = "<shift>+<insert>"
      data['abbreviation']['immediate'] = True;
      file.seek(0)        # <--- should reset file position to the beginning.
      json.dump(data, file, indent=4)
      file.truncate()     # remove remaining part