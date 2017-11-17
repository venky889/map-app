
function loadMapScenario() {
    var map = new Microsoft.Maps.Map(document.getElementById('myMap'), {});
    var pois;
    $.ajax({
      url: "/api/poi/",
      dataType: 'json',
      async: false,
      success: function(data) {
        pois = data;
      }

    });

    var pinLayer = new Microsoft.Maps.EntityCollection();
    var locs = [];
    for(var i = 0 ; i < pois.length; i++) {
      locs[i] = new Microsoft.Maps.Location(pois[i].lat, pois[i].lon);
      var pin = new Microsoft.Maps.Pushpin(locs[i]);
      pin.Title = pois[i].title;
      pin.Description = pois[i].location;
      pinLayer.push(pin);
    }
    console.log(locs)

    map.entities.push(pinLayer);
    var bestview = Microsoft.Maps.LocationRect.fromLocations(locs);
    map.setView({
      mapTypeId: Microsoft.Maps.MapTypeId.aerial,
      center: bestview.center,
    });

}
