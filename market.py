import requests
from operator import itemgetter


def buy_parse(pretty_input):
    x = 0
    outputDict = {}
    try:
        cleanInput= '_'.join(pretty_input)
        cleanInput = cleanInput.replace(' ', '_').lower()
        url = 'https://api.warframe.market/v1/items/' + cleanInput + '/orders'
        #url = 'https://api.warframe.market/v1/items/rhino_prime_blueprint/orders'  ##debug
        urlData = (requests.get(url))
        urlQuery = urlData.json()

        for i in urlQuery['payload']['orders']:
            if urlQuery['payload']['orders'][x]['order_type'] == 'sell' and \
                urlQuery['payload']['orders'][x]['platform'] == 'pc' and \
                urlQuery['payload']['orders'][x]['region'] == 'en' and \
                urlQuery['payload']['orders'][x]['user']['status'] == 'ingame':
                    plat = urlQuery['payload']['orders'][x]['platinum']
                    name = urlQuery['payload']['orders'][x]['user']['ingame_name']
                    outputDict[name] = plat
            x += 1

        sortedDict = sorted(outputDict.items(), key=itemgetter(1))
        trimmedTup = tuple(sortedDict[:5])
        return trimmedTup
    except KeyError:
        print('check spelling error')
        return []


def get_icon(pretty_input):

    try:
        cleanInput= '_'.join(pretty_input)
        cleanInput = cleanInput.replace(' ', '_').lower()
        url = 'https://api.warframe.market/v1/items/' + cleanInput + '/orders?include=item'
        urlData = (requests.get(url))
        urlQuery = urlData.json()
        iconURL = urlQuery['include']['item']['items_in_set'][0]['icon']
        cleanURL = 'https://warframe.market/static/assets/' + iconURL
        return cleanURL

    except KeyError:
        print('check spelling error')
        return []

def beautify_input(user_input):

    pretty_input = [x.lower() for x in user_input]
    #pretty_input = list(pretty_input)
    for n, item in enumerate(pretty_input):
        if item == 'p':
            pretty_input[n] = 'prime'
        if item == 'bp':
            pretty_input[n] = 'blueprint'

        if item == 'sys':
            pretty_input[n] = 'systems'
        if item == 'rec':
            pretty_input[n] = 'receiver'
        if item == 'bar':
            pretty_input[n] = 'barrel'
        if item == 'chas':
            pretty_input[n] = 'chassis'
        if item == 'helm':
            pretty_input[n] = 'neuroptics'
        if item == 'neur':
            pretty_input[n] = 'neuroptics'
        if item == 'gaunt':
            pretty_input[n] = 'gauntlet'
        if item == 'cere':
            pretty_input[n] = 'cerebrum'
        if item == 'cara':
            pretty_input[n] = 'carapace'
        if item == 'harn':
            pretty_input[n] = 'harness'
        if item == 'ul':
            pretty_input[n] = 'upper'
            pretty_input.append('limb')
        if item == 'll':
            pretty_input[n] = 'lower'
            pretty_input.append('limb')
        if item == 'a':
            pretty_input[n] = 'axi'
        if item == 'l':
            pretty_input[n] = 'lith'
        if item == 'n':
            pretty_input[n] = 'neo'
        if item == 'm':
            pretty_input[n] = 'meso'


    return tuple(pretty_input)

