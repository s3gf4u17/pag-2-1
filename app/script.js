markers = []

function setPointCoordinates(event,map,id) {
    new_markers = []
    markers.forEach(function(marker) {
        if (marker._id==id) map.removeLayer(marker);
        else new_markers.push(marker);
    })
    markers = new_markers
    var marker = L.marker(event.latlng);
    marker._id = id
    test = map.addLayer(marker);
    marker._icon.classList.add("huechange");
    markers.push(marker);
}

// function(e) {
//     var location = e.latlng;
//     var marker = L.marker(location).addTo(map);
//     marker._icon.classList.add("huechange");
//     // var popup = L.popup().setLatLng(location).setContent('<p>A</p>').openOn(map);
//     console.log("left click: ",location);
// }

function fetchVectorLayer(LC,input_layer,name){
    var color = getComputedStyle(document.documentElement).getPropertyValue('--accent');
    var layer = L.geoJSON(input_layer,{
        // onEachFeature:oEF,
        // pointToLayer:PToL
        style: {
            radius:5,
            opacity:0.2,
            color:'rgba(0,0,0,1.0)',
            weight:0.8
        }
    });
    LC.addOverlay(layer,name);
}

L.Control.Test = L.Control.extend({
    options: {
        position: "topleft"
    },
    initialize: function (options){
        // constructor
    },
    onAdd: function (map){
        // happens when added to map
        var parent = document.getElementById("map");
        var container = L.DomUtil.create("div","leaflet-control-layers leaflet-control-layers-expanded leaflet-control",parent);
        container.innerHTML = "<span class='title'>Geoportal - Wyznaczanie trasy</span></br>";
        container.innerHTML += "<span class='info'>1. Lewym przyciskiem myszy zaznacz <b style='color:deeppink'>punkt startowy</b>.</span></br>";
        container.innerHTML += "<span class='info'>2. Prawym przyciskiem myszy zaznacz <b style='color:dodgerblue'>punkt końcowy.</b></span></br>";
        container.innerHTML += "<span class='info'>3. Program wyznaczy trasę najkrótszą, najszybszą i alternatywną.</span>";
    }
});

function renderApp() {
    var map = L.map('map',{maxZoom:14,"zoomControl":false}).setView([53.0138,18.5984],10);
    var background = L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png',{maxZoom:50,attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'});
    background.addTo(map);
    var test = new L.Control.Test("12",{position:"topleft"});
    L.control.scale({"position":"bottomleft"}).addTo(map);
    L.control.zoom({"position":"bottomleft"}).addTo(map);
    map.on('click',function (e) {setPointCoordinates(e,map,'left-click')});
    map.on('contextmenu',function(e) {
        var location = e.latlng;
        var marker = L.marker(location).addTo(map);
        // var popup = L.popup().setLatLng(location).setContent('<p>B</p>').openOn(map);
        console.log("right click: ",location);
    });
    test.addTo(map);
}

