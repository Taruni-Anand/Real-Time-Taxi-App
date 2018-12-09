// Initialize and add the map
function initMap() {
  // The location of Uluru
  var uluru = {lat: 40.71139144897461, lng:-73.9468765258789};
  var dest = {lat: 40.721336364746094, lng:-73.93936920166014};

  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 13, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
  var marker2 = new google.maps.Marker({position: dest, map: map});
}
