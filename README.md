# GOAT

GOAT script that allows you to check prices of a specific sneaker based on SKU.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install discord_webhook and requests

[Python Discord Webhook API](https://pypi.org/project/discord-webhook/)
1. **Install Requirements**
```bash
$ cd GOAT_API_DIRECTORY
$ pip install -r requirements.txt
```
2. **To run**
```bash
$ cd GOAT_API_DIRECTORY
$ python api.py
```
## Usage
- In order to use the script, change the **pid** variable to any SKU.
- Input a valid **discord webhook** to send all data
```python
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_url = 'https://discordapp.com/api/webhooks/...'
webhook = DiscordWebhook(webhook_url)
pid = 'AJ4219-400'
```
[![](https://i.gyazo.com/0e81b26f30a585d8a6159e377dfef21a.gif)](https://gyazo.com/0e81b26f30a585d8a6159e377dfef21a)


## Future Updates
- Add GOAT recommendations from API
- Add UI

## License
[MIT](https://choosealicense.com/licenses/mit/)
