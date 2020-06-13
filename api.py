import json
import requests
import time
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_url = 'https://discordapp.com/api/webhooks/672159508675690497/4UtaClAc7rKMJsEvbR4iYf-Razv4M3ZWtkYDOxBzLfiDzJhI7RSFpoLn6iijBiRcaNOR'
webhook = DiscordWebhook(webhook_url)
pid = '508214-660'
headers = {
    'Connection': 'keep-alive',
    'accept': 'application/json',
    'Origin': 'https://www.goat.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.goat.com/search?query='+ pid,
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

params = {
    'x-algolia-agent': 'Algolia for vanilla JavaScript 3.25.1',
    'x-algolia-application-id': '2FWOTDVM2O',
    'x-algolia-api-key': 'ac96de6fef0e02bb95d433d8d5c7038a',
}

data = {
    "distinct": 'true',
    'facetFilters': 'product_category: shoes',
    'facets': 'size',
    'hitsPerPage': '48',
    'numericFilters': '[]',
    'page': '0',
    'query': pid,
    'clickAnalytics': "true"
}
response = requests.post('https://2fwotdvm2o-dsn.algolia.net/1/indexes/product_variants_v2/query', headers=headers, params=params,json=data)
response_json = response.json()
response_json_dict = response_json['hits'][0]
product_id = response_json_dict['product_template_id']
print(product_id)

def obtainBasicInfo():
    webhook = DiscordWebhook(url=webhook_url)
    r_api = requests.get('https://www.goat.com/web-api/v1/product_variants?productTemplateId='+ str(product_id),headers=headers)
    data = r_api.json()
    embed = DiscordEmbed(title=response_json_dict['name'], url=headers['Referer'], color=242424)
    embed.set_thumbnail(url=response_json_dict['main_picture_url'])
    sizes = []
    shoe_conditions = []
    box_conditions = []
    prices = []
    for i in data:
        sizes.append(str(i['size']))
        shoe_conditions.append(i['shoeCondition'])
        box_conditions.append(i['boxCondition'])
        prices.append(str(int(i['lowestPriceCents']['amountUsdCents'])/100))
        print(' Size: ' + str(i['size']) + '\n' + ' Shoe condition: ' + i['shoeCondition'] + '\n' + ' Box condition: ' + i['boxCondition'] + '\n' + ' $' + str(int(i['lowestPriceCents']['amountUsdCents'])/100) + '\n' + '-----------------')
        embed.add_embed_field(name='Size', value=(str(i['size'])))
        embed.add_embed_field(name='Shoe Condition', value=str(i['shoeCondition']))
        embed.add_embed_field(name='Box Condition', value=str(i['boxCondition']))
        embed.add_embed_field(name='Price', value='$' + str(int(i['lowestPriceCents']['amountUsdCents'])/100))
        webhook.add_embed(embed)
        send_hook = webhook.execute()
        time.sleep(2)
        embed.fields = []
    print(sizes)
    print(shoe_conditions)
    print(box_conditions)
    print(prices)


obtainBasicInfo()
