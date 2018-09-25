import requests
from market import buy_parse


def relic_parse(user_input):
    try:
        input_list = [x.title() for x in user_input]
        url_data = requests.get('https://drops.warframestat.us//data/relics/{}/{}.json'.format(input_list[0],input_list[1]))
        url_json = url_data.json()
        relic_drops = []

        for x, item in enumerate(url_json['rewards']['Intact']):
            relic_drops.append(url_json['rewards']['Intact'][x]['itemName'])

        #print(relic_drops)
        ex_strings = ['Systems', 'Chassis', 'Neuroptics', 'Harness', 'Wings']

        relic_drop_command = [item.strip(' Blueprint').lower() if any(x in item for x in ex_strings) else item.lower() for item in relic_drops]

        for n, item in enumerate(relic_drop_command):
           relic_drop_command[n] = tuple(item.split())

        item_prices = []

        for n, item in enumerate(relic_drop_command):

            offers = buy_parse(item)
            #print(offers)
            plat = []
            if len(offers) != 0:
                for i in offers:
                    plat.append(i[1])
                plat = int(sum(plat)/len(plat))
                item_prices.append(str(plat)+' p')
            else:
                item_prices.append('n/a')

        embed_body = ''
        for n, item in enumerate(relic_drops):
            embed_body += '{}  |  {}\n'.format(item, item_prices[n])
    except:
        pass

    #print(embed_body)

    return embed_body

