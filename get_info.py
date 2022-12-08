import requests
import credentials
#from wordcloud import WordCloud
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

    #fig_reviews = go.Figure([go.Bar(x=tiendas, y=avg_tienda)])
    #fig_total = go.Figure([go.Bar(x=tiendas, y=totales)])
    #fig_reviews.show()
    #fig_total.show()
    print(totales)
    '''
    fig, ax = plt.subplots()
    meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', ]
    calificaciones = {'oxxo': [4.3, 5, 3.3, 3.7, 4.8, 4.3, 3.2, 3.1, 2.9, 4.1, 4, 3]}
    ax.plot(meses, calificaciones['oxxo'], label='oxxo')
    ax.legend(loc='upper right')
    plt.show()

    fig, ax = plt.subplots()
    meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', ]
    calificaciones = {'7 eleven': [3.5, 1.7, 3.8, 3, 4, 3.4, 2.2, 3.1, 2.9, 4.1, 3.3, 3]}
    ax.plot(meses, calificaciones['7 eleven'], label='7 eleven')
    ax.legend(loc='upper right')
    plt.show()

    fig, ax = plt.subplots()
    meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', ]
    calificaciones = {'modelorama': [4.3, 4.4, 4.7, 4.5, 4.3, 4.8, 4.8, 4.3, 4.1, 4.1, 4.3, 4.2]}
    ax.plot(meses, calificaciones['modelorama'], label='modelorama')
    ax.legend(loc='upper right')
    plt.show()

    fig, ax = plt.subplots()
    meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', ]
    calificaciones = {'Extra': [4, 3.8, 3.5, 3.4, 3, 2.3, 3.6, 4.1, 4.3, 4.5, 5, 4]}
    ax.plot(meses, calificaciones['Extra'], label='Extra')
    ax.legend(loc='upper right')
    plt.show()

    fig, ax = plt.subplots()
    meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', ]
    calificaciones = {'Circle k': [4, 3.7, 4, 3.8, 2.7, 3.6, 4.2, 4.1, 3.9, 3.6, 4.3, 3]}
    ax.plot(meses, calificaciones['Circle k'], label='Circle k')
    ax.legend(loc='upper right')
    plt.show()

    fig, ax = plt.subplots()
    meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', ]
    calificaciones = {'pick & go': [4.5, 4.6, 4.7, 4.8, 5, 4.9, 4.7, 4.8, 4.8, 4.6, 4.7, 5]}
    ax.plot(meses, calificaciones['pick & go'], label='pick & go')
    ax.legend(loc='upper right')
    plt.show()

    fig, ax = plt.subplots()
    meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',]
    calificaciones = {'oxxo': [4.3, 5, 3.3, 3.7, 4.8, 4.3, 3.2, 3.1, 2.9, 4.1, 4, 3],
                    '7 eleven': [3.5, 1.7, 3.8, 3, 4, 3.4, 2.2, 3.1, 2.9, 4.1, 3.3, 3],
                    'modelorama': [4.3, 4.4, 4.7, 4.5, 4.3, 4.8, 4.8, 4.3, 4.1, 4.1, 4.3, 4.2],
                    'Extra': [4, 3.8, 3.5, 3.4, 3, 2.3, 3.6, 4.1, 4.3, 4.5, 5, 4],
                    'Circle k': [4, 3.7, 4, 3.8, 2.7, 3.6, 4.2, 4.1, 3.9, 3.6, 4.3, 3],
                    'pick & go': [4.5, 4.6, 4.7, 4.8, 5, 4.9, 4.7, 4.8, 4.8, 4.6, 4.7, 5]}
    ax.plot(meses, calificaciones['oxxo'], label='oxxo')
    ax.plot(meses, calificaciones['7 eleven'], label='7 eleven')
    ax.plot(meses, calificaciones['modelorama'], label='modelorama')
    ax.plot(meses, calificaciones['Extra'], label='Extra')
    ax.plot(meses, calificaciones['Circle k'], label='Circle k')
    ax.plot(meses, calificaciones['pick & go'], label='pick & go')
    ax.legend(loc='upper right')
    plt.show()
    '''