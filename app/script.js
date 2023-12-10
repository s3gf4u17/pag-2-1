var markers = [];
var layer = null;

function findPath(map) {
    // fetch path geojson
    const settings = {
        method:"POST",
        headers: {"content-type": "application/json"},
        body: JSON.stringify({
            lat0:markers[0]._latlng.lat,
            lon0:markers[0]._latlng.lng,
            lat1:markers[1]._latlng.lat,
            lon1:markers[1]._latlng.lng
        })
    };
    // const geojson = fetch("http://127.0.0.1:8000/test_line/",settings)
    const geojson = fetch("http://127.0.0.1:8000/test_point/",settings)
    .then(response=>response.json())
    .then(geojson=>{
        console.log(geojson);
        if (layer!=null) map.removeLayer(layer);
        layer = L.geoJSON(geojson,{style:{
            radius:5,
            opacity:1.2,
            color:'rgba(0,0,0,1.0)',
            weight: 5.8
        }});
        map.addLayer(layer);
    });
}

function setMarker(event,map,id) {
    // delete old marker associated with 'id'
    new_markers = []
    markers.forEach(function(marker) {
        if (marker._id==id) map.removeLayer(marker);
        else new_markers.push(marker);
    })
    // create new marker in its place
    markers=new_markers
    var marker = L.marker(event.latlng);
    marker._id = id;
    handle = map.addLayer(marker);
    if (id=="left-click") marker._icon.classList.add("huechange");
    markers.push(marker);
    console.log(marker);
    if (markers.length==2) findPath(map);
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
        container.innerHTML += "<span class='info'>3. Program wyznaczy trasę <b style='color:#bc5090'>najkrótszą</b>, <b style='color:#ff6361'>najszybszą</b> i <b style='color:#ffa600'>alternatywną</b>.</span>";
    }
});

function renderApp() {
    var map = L.map('map',{maxZoom:19,"zoomControl":false}).setView([53.0138,18.5984],13);
    var background = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19,attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'});
    background.addTo(map);
    var test = new L.Control.Test("12",{position:"topleft"});
    L.control.scale({"position":"bottomleft"}).addTo(map);
    L.control.zoom({"position":"bottomleft"}).addTo(map);
    map.on('click',function (e) {setMarker(e,map,'left-click')});
    map.on('contextmenu',function(e) {setMarker(e,map,'right-click')});
    test.addTo(map);
}

