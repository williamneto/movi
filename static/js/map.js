var geocoder;
var map;
var markers = [];

function geocodeAddress(geocoder, resultsMap, address, title, id) {
  geocoder.geocode({'address': address}, function(results, status) {
    if (status === google.maps.GeocoderStatus.OK) {
      resultsMap.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
        map: resultsMap,
        position: results[0].geometry.location,
        title: title
      });

      marker.addListener('click', function() {
        map.setZoom(13);
        map.setCenter(marker.getPosition());
        $("#movi_"+id).modal();
      });

      obj = {
        'id': id,
        'marker': marker
      }
      markers.push(obj)
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

  map.addListener('center_changed', function() {
    // 3 seconds after the center of the map has changed, pan back to the
    // marker.
    window.setTimeout(function() {
      map.panTo(marker.getPosition());
    }, 3000);
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
                geocodeAddress(geocoder, map, ad, data[i].nome, data[i].id)
              } else {
                geocodeAddress(geocoder, map, data[i].cidade, data[i].nome, data[i].id)
              }
            }
          }
      });

      $(".movi_drop").click(function(){
        var movi_id = $(this).attr('id')
        $.ajax({
            url: ".",
            type: "GET",
            data: {"cmd": "drop_movi", "id": movi_id},
            success: function(data){
              alert("Informação excluida!");
              $("#movi_"+movi_id).modal('toggle');
              window.location.reload(true); 
            }
        });
      });

      $("#new_nota_form").submit(function(){
        $.ajax({
            type: 'POST',
            cache: false,
            url: '.',
            data: $(this).serialize(), 
            success: function(msg) {
                alert("Nota salva!");
                $("#new_nota_form").trigger('reset');
                $("#new_note_modal").modal('toggle');
            }
        });
        return false;
      });
})