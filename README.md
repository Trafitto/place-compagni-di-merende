# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Place Compagni Di Merende serves beautiful images of our trio of best friends, 
for the purpose of using them as placeholders for your sites.

## Getting Started <a name = "getting_started"></a>

The app use Flask as server.


Build the project with docker compose: 

`docker-compose -f docker-compose.yml build`


Lunch the container with:

`docker-compose -f docker-compose.yml up`


and go to `0.0.0.0:5000` to se the homepage

for the API `0.0.0.0:5000/place`


## Usage <a name = "usage"></a>

You will get a random image of the [Snack Companions](https://en.wikipedia.org/wiki/Monster_of_Florence)

##### Simple use

Use in your html img tag

`<img src="http://0.0.0.0:5000/place">`

##### You can have one! Go on, choose!!

You can also specify your favorite companion by adding it to the url

`<img src="http://0.0.0.0:5000/place/pacciani">`

The choice is between `/pacciani`, `/vanni`, `/lotti`

##### Query Params

The optional query params are `width` and `height`,


`<img src="http://0.0.0.0:5000/place?width=500&height=500">`

Give us an image of 500X500 px

Note: 

if only one of the two was passed the image would be automatically restricted while maintaining the ratio
