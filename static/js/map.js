var geocoder;
var map;

function geocodeAddress(geocoder, resultsMap, address, title) {
  geocoder.geocode({'address': address}, function(results, status) {
    if (status === google.maps.GeocoderStatus.OK) {
      resultsMap.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
        map: resultsMap,
        position: results[0].geometry.location,
        title: title
      });
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat:  -22.9068467, lng: -43.1728965},
    zoom: 10
  });
  geocoder = new google.maps.Geocoder();


  
  var infowindow = new google.maps.InfoWindow();
  var marker = new google.maps.Marker({
    map: map,
    anchorPoint: new google.maps.Point(0, -29)
  });
}

$(document).ready(function(){
      $.ajax({
          url: ".",
          type: "GET",
          data: {"cmd": "get_movi_data"},
          success: function(data){

            for (var i = 0; i < data.length; i++){
              if (data[i].cidade && data[i].bairro) {
                ad = data[i].cidade + "," + data[i].bairro
                geocodeAddress(geocoder, map, ad, data[i].nome)
              } else {
                geocodeAddress(geocoder, map, data[i].cidade, data[i].nome)
              }
            }
          }
      });
})