# {Place Compagni di Merende}

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/0-percent-optimized.svg)](https://forthebadge.com)


## About 

Place Compagni Di Merende serves beautiful images of our trio of best friends, 
for the purpose of using them as placeholders for your sites.

## Usage 

You will get a random image of the [Snack Companions](https://en.wikipedia.org/wiki/Monster_of_Florence)

##### Simple use

Use in your html img tag

`<img src="http://0.0.0.0:5000/place">`

##### You can have one! Go on, choose!!

Specify your favorite companion by adding it to the url

`<img src="http://0.0.0.0:5000/place/pacciani">`

The choice is between `/pacciani`, `/vanni`, `/lotti`

##### Query Params

The optional query params are `width` and `height`,

`<img src="http://0.0.0.0:5000/place?width=500&height=500">`

the maximum size of the photos is 2000x2000px

Note: 

If only one of the two params was passed the image would be automatically resize while maintaining the ratio


## Getting Started 

#### Still in development

It is basically a Flask webserver, you can use Doker and docker-compose.

[![forthebadge](https://forthebadge.com/images/badges/works-on-my-machine.svg)](https://forthebadge.com)

Build the project with docker compose: 

`docker-compose -f docker-compose.yml build`


Up the container with:

`docker-compose -f docker-compose.yml up`


and go to `0.0.0.0:5000` to se the homepage

for the API `0.0.0.0:5000/place`

