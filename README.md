# Project Aurora
This project focuses on the Google Maps Platform APIs with Postman with the post and get methods to find the mini-supermarkets best rated by users in the city of Morelia, Michoacán, México (19.70078, -101.18443) within a radius of 10 km from the aforementioned area. We worked with only 6 of the "best" known stores in Mexico, which are oxxo, 7 eleven, modelorama, Extra, Circle k and pick & go.

Doing a first search of the various establishments, I realize that the store that has the highest number of reviews by users is pick & go
but there is a possibility that I find myself analyzing stores that are not in service, for this I add a validation
using the field STATUS != 'OPERATIONAL' this tells me that there is only one store that is no longer in operation that is in
C. de Bucareli 1115, Vasco de Quiroga, Morelia' extra store, after reviewing this store, I realized that there are no reviews
for her, so it does not affect my preliminary analysis.

In conclusion, the best rated store with the most user reviews is pick & go.

# Number of users
[![users.png](https://i.postimg.cc/bNQsgvHs/users.png)](https://postimg.cc/XpYj74Pb)
Number of users who rate the stores 2022.

# Ratings of the stores
[![ratings.png](https://i.postimg.cc/g2mrTPN4/ratings.png)](https://postimg.cc/56KxXDcF)
Number of store ratings 2022.

