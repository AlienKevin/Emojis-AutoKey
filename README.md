# Emojis-AutoKey
The easiest and quickest🚀 way to insert emojis on Linux🐧.

# Functionalities
Insert any Unicode emojis by typing :emoji_name: and Emojis-AutoKey automatically replace them with the emoji.
e.g. `:smile:` => 😄, `:moon:` => 🌔, [1480+ more emojis](https://unicodey.com/emoji-data/table.htm)
Emojis-AutoKey works in Google Chrome search bar, text editors like gedit, address bar on top of the File Explorer.
Emojis-AutoKey does *not* work in the Terminal and search bar of "Show Applications"

# Installation
1. Install [AutoKey](https://github.com/autokey/autokey#installation) first
2. Open AutoKey
3. Clone or Download this repo
4. Copy all files in the `emoji-phrases` folder and paste them into `My Phrases` folder in AutoKey or any other folders you created in `/home/<USERNAME>/.config/autokey/data`
5. AutoKey will display a message box that configurations are changed
5. Quit AutoKey by pressing <kbd>Ctrl</kbd>+<kbd>Q</kbd> then restart it
6. Start using Emojis-AutoKey

# build
1. Install [AutoKey](https://github.com/autokey/autokey#installation) first
2. Edit the `Emojis.python` file and replace folder name in the line `folder = engine.get_folder("My Phrases")` with your own and change the `json_file_name` with your own `json_file_name = "/home/kevin/.config/autokey/data/My Phrases/." + title + ".json`.
3. Run the python script in AutoKey by pressing the green play button on the top bar
4. Wait for about 2 minutes until the script finishes and restart AutoKey

# Credits
This project is heavily based on [emoji-to-ahk](https://github.com/alexmick/emoji-to-ahk) created by [alexmick](https://github.com/alexmick) and thank you [josephj11](https://github.com/josephj11) for teaching me how to use AutoKey.

# License
This project is licensed under the terms of the MIT License.


