# Project Aurora
[![aurora-polar-en-las-montanas-8458.jpg](https://i.postimg.cc/nzJ60pQQ/aurora-polar-en-las-montanas-8458.jpg)](https://postimg.cc/v10qmRhQ)

# Author
Carlos Daniel Camilo Aguilar

# Contact
mordexcamiloaguilar878689@gmail.com

# License
GNU General Public License v3.0

# Installation
To install simply download the zip file of the code or copy it into your preferred IDE and through your terminal install the following libraries with the command pip install " "
- ipython
- requests
- credentials
- matplotlib
- ploty

# Ejecution
Once you have everything installed open the ipython shell and run the file in your terminal.
[![Screenshot-121.png](https://i.postimg.cc/v8g6yy1V/Screenshot-121.png)](https://postimg.cc/z3Nfw9Fz)


# Introduction
This project focuses on the Google Maps Platform APIs worked with the Postman program with the post and get methods to find the best rated supermarkets-expres by users in the city of Morelia, Michoacán, Mexico (19.70078, -101.18443) in a radius of 10 km from the center of the aforementioned area. We work with only 6 of the "most" known stores in Mexico, which are oxxo, 7 eleven, modelorama, Extra, Circle k and pick & go.


# Metodology
Scientific method.

# Implementation
It can be implemented to compare store statistics and the conclusion of the user if the experience was pleasant, cleanliness of the establishment, treatment of the workers to the user, knowing what is good and what is bad. All this can be as a web service, in an application, even any company can integrate it into its system in order to be more competitive with its competition.

# Tests
Doing a first search among the different establishments, I realize that the store that has the greatest number of opinions from users is pick & go
but there is a possibility that I find myself analyzing stores that are not in service, for this I add a validation
using the field STATUS != 'OPERATIONAL' this tells me that there is only one store that is no longer in operation that is in
C. de Bucareli 1115, Vasco de Quiroga, extra store in Morelia, after reviewing this store I realized that there are no reviews
for her, so it does not affect my preliminary analysis.

# Results
[![Figure-todos.png](https://i.postimg.cc/RZ8m1kRc/Figure-todos.png)](https://postimg.cc/DSqRnYRZ)

Number of store ratings 2021.

# Conclusions
In conclusion, the best rated store with the most user reviews is pick & go.

# Bibliogtraphy
- https://github.com/googlemaps/google-maps-services-python
- https://www.google.com.mx/maps?hl=es-419&tab=rl
- https://developers.google.com/maps

