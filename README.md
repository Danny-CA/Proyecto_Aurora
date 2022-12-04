# Project Aurora
Este proyecto se centra en base a APIs de Google Maps Platform para encontrar los mini super mejor calificados por los usuarios en la ciudad de Morelia, Michoacán, México (19.70078, -101.18443) en un radio de 10 km del área ya mencionada. Se trabajó con sólo 6 de las tiendas "mejor" conocidas que son oxxo, 7 eleven, modelorama, Extra, Circle k y pick & go.
Haciendo una primer busqueda de los diversos establecimientos, me percato que la tienda que tiene mayor numero de reviews por usuarios es pick & go
pero existe la posibilidad de que me encuentre analizando tiendas que no estan en servicio, para ello agrego una validación
utilizando el campo STATUS != 'OPERATIONAL' este me indica que solo existe una tienda que ya no esta en operación que se encuentra en 
C. de Bucareli 1115, Vasco de Quiroga, Morelia' tienda extra,  despues de revisar esta tienda, me percato que no existe ningun review
para ella, por lo que no afecta en mi análisis preeliminar.
En conclusión la tienda mejor calificada y con más reseñas de usuarios es pick & go.
# Number of users
[![users.png](https://i.postimg.cc/bNQsgvHs/users.png)](https://postimg.cc/XpYj74Pb)
Number of users who rate the stores 2022.

# Ratings of the stores
[![ratings.png](https://i.postimg.cc/g2mrTPN4/ratings.png)](https://postimg.cc/56KxXDcF)
Number of store ratings 2022.

