
function loadMapScenario() {
    var map = new Microsoft.Maps.Map(document.getElementById('myMap'), {});
    var pois;
    var roads;
    var buildings;
    var locations = []

    $.ajax({
      url: "/api/poi/",
      dataType: 'json',
      async: false,
      success: function(data) {
        pois = data;
      }
    });
    console.log(roads)

    $.ajax({
      url: "/api/road/",
      dataType: 'json',
      async: false,
      success: function(data) {
        roads = data;
      }
    });
    console.log(roads)

    $.ajax({
      url: "/api/building/",
      dataType: 'json',
      async: false,
      success: function(data) {
        buildings = data;
      }
    });
    console.log(buildings)

    var pushpinImage = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAEPUlEQVR42pWVf0idVRjHn/Oc933vVSNzuUg3G4Z/xHJWTKklTZuTivWLiigcUaMQ22otBssY6w+zYCtKa4NYP5i0ZFKy6aotqRxs5VhGEtSmuX74c9pSN/Xe977nPKfnuBtJ5PX6wOGc917O9/P8fF8B89jOvmhauisrsjxRHkbINQAmSnB2yDdHJ5T6aFtOSjTRfZHoz7phtT7bgToFsGg0AIgZAxbgCiEyHQAJZmRIiarns5zmBQN2DQbbMyTUDAbGhBFFWBpwBYI2QFFtMEpEPglc6gH8pcxz1Uu9uqQBO/rU3ZdLah1XhlJZPNURJlUKCEuEgEhMaWOmtRHTRMbXHI00Yiwwt7+SG26fF/DU8V6RnbOkN2Iw13odFkipLmJYB3CuqxMUCspcsRIjgBQh4EgMKMVRkvqpNi8tf17Asz2R8rCELwx7G0IBIYl0/vuT2LJlA0QnxrgChlIyF+O6+gZKv64AY8S10UTgK/QN3LJn+WUnEwI2/jxZIxG3eyFJLgMgMima1t1syPdBSgkopb1jMDVN3HfwhCHHhSAg4UdjgjHb3ilI35kQUPnjhXelgxtCnhSuK6G/rZW+2bEZ3VDoEkAI4gMKranw5bcxs3A1xAJFsahCRfTmezdlbEkIePKH8d0ooSrkucL1HBg40kydr76AjgU4joUQshnuooIXd2FGYQkEfkB+LGAAvN5QdOXWhIDHvxvbJAW95YZcch0EmjgvvqxYazg1ID0PuN5CSMc47EDRnoNGh1I4RVoEMS2UNpv3r1pcnxBQ8e1IHmv0eJwex2FRV5J/rAVP1deC4Ag816VQOIz5VdUEN96GKtAWQLGYQhBY2Fh8Vee8c/Do8XNfsVap4zjGpttx0GRODEOkqwOE6whvxSozmrpIaHZZcV5UTFnvTzeVZi9PatAePjZ8K7fjCddlp7hNUQqbGADbVQTEnco1MKQ0IQUEXGP7Crm/uWzJoaQA1h5o62tk8Uc4S1xUDsNKIDKAx5dzQZrLzCBuJuD1yaE7lj30fzpzAu75/PdMYaAbHXEFy3Jh0Q6ZPc1EoMn2EY+z0gNCyvzDdy0bXxDA2p2tvz7Gqvski86KQBghmGF4sIzgYNYcuTf367k0EgKslX18pp23EsR/I2DjBzBTQ3/s7XimvDLR/XkBqw+cKTBad836iRiC5EfGOjaWFuipC/yCAv5kgI4vE9c1SQGsrTnQ08B9sh5m6stJ4cJ076ut7v/0g/fjohYQzMAv7TrpCKytbTx9jeN6v7DnrvUs+ufQb+2VxeV8jM0CqFmgfyAmKYC1kjeO7k6/9vqn2X3ofG3T1v5jzYdniVuQzysa39WCIrBW/NKHV2cVlZ2dHh0c+eyJlQ/GRSO8LvKajIvr/95LGmCttKapbvBU21R3y979/GiLOx4XprnuLAiQkXdDzsWBXldFJofj3pv57vwNg4wHNyaxjt4AAAAASUVORK5CYII='

    function loadPins() {
      var pinLayer = new Microsoft.Maps.EntityCollection();
      var locs = [];
      for(var i = 0 ; i < pois.length; i++) {
        locs[i] = new Microsoft.Maps.Location(pois[i].lat, pois[i].lon);
        locations.push(locs[i]);
        console.log('loc1');
        console.log(locs[i]);
        console.log('loc2');
        console.log(locations);
        var pin = new Microsoft.Maps.Pushpin(locs[i], {
          icon: pushpinImage,
          anchor: new Microsoft.Maps.Point(12, 24)
        });
        pin.Title = pois[i].title;
        pin.Description = pois[i].location;
        pinLayer.push(pin);
      }
      map.entities.push(pinLayer);
    }

    function loadLines() {
      var lineLayer = new Microsoft.Maps.EntityCollection();
      for (var r = 0 ; r < roads.length; r++) {
        var locs = [];
        for (var l = 0 ; l < roads[r].coords.length; l++) {
          console.log(roads[r].coords)
          var lat = roads[r].coords[l]['lat'];
          var lon = roads[r].coords[l]['lon'];
          console.log(lat)
          locs[l] = new Microsoft.Maps.Location(lat, lon);
          locations.push(locs[l]);
          console.log('loc3');
          console.log(locs[l]);
          console.log('loc4');
          console.log(locations);
        }
        var line = new Microsoft.Maps.Polyline(locs, {
          strokeColor: 'orangered',
          strokeThickness: 3
        });
        // line.Name = roads[r].name;
        // line.Description = roads[r].speed_limit;
        lineLayer.push(line);
      }
      map.entities.push(lineLayer);
    }

    function loadPolygons() {
      var polyLayer = new Microsoft.Maps.EntityCollection();
      for (var b = 0 ; b < buildings.length; b++) {
        var locs = [];
        for (var l = 0 ; l < buildings[b].coords.length; l++) {
          var lat = buildings[b].coords[l]['lat'];
          var lon = buildings[b].coords[l]['lon'];
          locs[l] = new Microsoft.Maps.Location(lat, lon);
          locations.push(locs[l]);
          console.log('loc5');
          console.log(locs[l]);
          console.log('loc6');
          console.log(locations);
        }
        var polygon = new Microsoft.Maps.Polygon(locs, {
          strokeColor: 'black',
          fillColor: 'mediumspringgreen',
          strokeThickness: 1
        });
        // polygon.Name = buildings[b].name;
        // polygon.Description = buildings[b].number;
        polyLayer.push(polygon);
      }
      map.entities.push(polyLayer);
    }
    
    loadPins()
    loadLines()
    loadPolygons()
    console.log(locations)
    var bestview = Microsoft.Maps.LocationRect.fromLocations(locations);
    map.setView({
      mapTypeId: Microsoft.Maps.MapTypeId.aerial,
      bounds: bestview
    });

}
