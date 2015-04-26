var map1;
var map;
var rad;
var myCenter1;
var myCenter=new google.maps.LatLng(12.9667,77.5667);
var jaaga = new Array();
var hesru = new Array();
var addressu = new Array();
var djangslon=new Array();
var djangslat=new Array();
var final=new Array();
var i=0;
var j=0;
function lungi_dance() {
  var mapProp = {
    center:myCenter1,
    zoom:10,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  
  var myCity = new google.maps.Circle({
  center:myCenter1,
  radius:res,
  strokeColor:"#0000FF",
  strokeOpacity:0.8,
  strokeWeight:2,
  fillColor:"#0000FF",
  fillOpacity:0.4
  });

   map1=new google.maps.Map(document.getElementById("googleMaps"),mapProp);
   placeMarkerModal(myCenter1);
   myCity.setMap(map1);
}


function initialize()
{
var mapProp = {
  center:myCenter,
  zoom:10,
  mapTypeId:google.maps.MapTypeId.ROADMAP
  };
map = new google.maps.Map(document.getElementById("googleMap"),mapProp);

 var infowindow = new google.maps.InfoWindow();
  var marker = new google.maps.Marker({
    map: map,
    anchorPoint: new google.maps.Point(0, -29)
  });
  
  google.maps.event.addListener(map, 'click', function(event) {
    
    placeMarker(event.latLng);



    var myCity = new google.maps.Circle({
  center:event.latLng,
  radius:10000,
  strokeColor:"#0000FF",
  strokeOpacity:0.8,
  strokeWeight:2,
  fillColor:"#0000FF",
  fillOpacity:0.4
  });
//myCity.setMap(map);
  });
  var search=document.getElementById("search");

  var autocomplete = new google.maps.places.Autocomplete(search);
  autocomplete.bindTo('bounds', map);
  google.maps.event.addListener(autocomplete, 'place_changed', function() {
    
    var place = autocomplete.getPlace();
    if (!place.geometry) {
      return;
    }

    // If the place has a geometry, then present it on a map.
    if (place.geometry.viewport) {
      map.fitBounds(place.geometry.viewport);
    } else {
      map.setCenter(place.geometry.location);
      map.setZoom(14);  // Why 17? Because it looks good.
    }
    marker.setIcon(/** @type {google.maps.Icon} */({
      url: place.icon,
      size: new google.maps.Size(71, 71),
      origin: new google.maps.Point(0, 0),
      anchor: new google.maps.Point(17, 34),
      scaledSize: new google.maps.Size(35, 35)
    }));
    jaaga[i]=place.geometry.location;
    djangslat[j]=jaaga[i].lat();
  djangslon[j]=jaaga[i].lng();
  j=j+1;
    marker.setPosition(place.geometry.location);
    marker.setVisible(true);
    
    if(i>=1)
{
placeNameMarker(jaaga[i-1],hesru[i-1],addressu[i-1]);
 }
    var address = '';
    if (place.address_components) {
      address = [
        (place.address_components[0] && place.address_components[0].short_name || ''),
        (place.address_components[1] && place.address_components[1].short_name || ''),
        (place.address_components[2] && place.address_components[2].short_name || '')
      ].join(' ');
    }
hesru[i]=place.name;
addressu[i]=address;
    infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
    infowindow.open(map, marker);
    search.value="";
i=i+1;
  });

}
function placeNameMarker(location,name,address) {
  var marker = new google.maps.Marker({
    position: location,
    map: map,
  });
  
  var infowindow = new google.maps.InfoWindow({
    content: '<div><strong>' + name + '</strong><br>' + address
  });
  infowindow.open(map,marker);
  search.value="";
}

function placeMarker(location) {
  var marker = new google.maps.Marker({
    position: location,
    map: map,
  });
  var infowindow = new google.maps.InfoWindow({
    content: 'Latitude: ' + location.lat() + '<br>Longitude: ' + location.lng()
  });
  djangslat[j]=location.lat();
  djangslon[j]=location.lng();
  j=j+1;
  infowindow.open(map,marker);
 
}
function placeMarkerModal(location) {
  var marker = new google.maps.Marker({
    position: location,
    map: map1,
  });
  var infowindow = new google.maps.InfoWindow({
    content: 'Latitude: ' + location.lat() + '<br>Longitude: ' + location.lng()
  });
 
  infowindow.open(map1,marker);
 
}
function callback(results, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    for (var i = 0; i < results.length; i++) {
      var place = results[i];
      createMarker(results[i]);
    }
  }
}
google.maps.event.addDomListener(window, 'load', initialize);
function getCookie(name) {
var cookieValue = null;
if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
console.log(csrftoken);

//Ajax call
function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
   beforeSend: function(xhr, settings) {
   if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
     xhr.setRequestHeader("X-CSRFToken", csrftoken);
   }
   }});



$(document).ready(function(){

$('#myModal').on('shown', function () {
  google.maps.event.trigger(map1, 'resize');
})

    $("#process").click(function(){



        $.ajax({
          url: "",
          type:"POST",
          data:{lat:djangslat,lag:djangslon},
         // contentType: "application/json",
          //contentType: "json"
          success: function(result){

res=result['dist']*1000;
          initialize();
        //alert(result);
        myCenter1=new google.maps.LatLng(result['x'],result['y']);
        lungi_dance();
        for(var i=0;i<djangslat.length;i++)
{
placeMarkerModal(new google.maps.LatLng(djangslat[i],djangslon[i]));
}
$('#myModal').modal('show');
final = result['place'].slice();
 alert(final);
//final=result['place'];
for(var i=0;i<final.length;i++)
{

//{{% for var in result %}}
  $("#list").append("<li class='list-group-item'>"+final[i]+"</li>");
//{{% endfor %}}
}
    }
  });
    });
});