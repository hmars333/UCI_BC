// Creating map object
var myMap = L.map("map", {
    center: [40.7, -73.95],
    zoom: 11
  });


// Adding tile layer to the map
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
maxZoom: 18,
id: 'mapbox/outdoors-v11',
accessToken: API_KEY
});



// Base URL
var url="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson";


d3.json(url, function(data) {


};
