import requests
import credentials
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import plotly.graph_objects as go

def get_store(key, location):
    global credentials
    rango = 10000
    credentials.key = 'AIzaSyCEaSq-_EXcXMTbhOVZQ07tI-Psj_aaSjc'
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword={}&location={}&radius={}&key={}".format(key, location, rango, credentials.key)

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    tienda = response.json()
    total = 0
    ratings = []
    categories = []
    for i in range(len(tienda["results"])):
        ratings.append(tienda["results"][i]["rating"])
        total += tienda["results"][i]["user_ratings_total"]
        categories.append(tienda["results"][i]['types'])
        status = tienda["results"][i]['business_status']
        if status != 'OPERATIONAL':
            print(status, tienda["results"][i], key)
    return total, ratings, categories

if __name__ == '__main__':
    tiendas = ['oxxo', '7 eleven', 'modelorama', 'Extra', 'Circle k', 'pick & go']
    loc = '19.7028943,-101.1957545'
    avg_tienda = []
    totales = []
    categories = []
    for tienda in tiendas:
        total, rating, cat = get_store(tienda, loc)
        avg_tienda.append(sum(rating) / len(rating))
        totales.append(total)
        categories.append(cat)
    for cat_store in categories:
        text = ''
        for category in cat_store[0]:
            text = text + ' ' + category

    fig_reviews = go.Figure([go.Bar(x=tiendas, y=avg_tienda)])
    fig_total = go.Figure([go.Bar(x=tiendas, y=totales)])
    fig_reviews.show()
    fig_total.show()