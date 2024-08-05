/*OpenStreetMap*/

	var map = L.map('map').setView([51.505, -0.09], 13);

	var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
			'Imagery � <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1
	}).addTo(map);

	var marker = L.marker([51.5, -0.09]).addTo(map)
		.bindPopup('<b>Hello world!</b><br />I am a popup.').openPopup();

	var circle = L.circle([51.508, -0.11], {
		color: 'red',
		fillColor: '#f03',
		fillOpacity: 0.5,
		radius: 500
	}).addTo(map).bindPopup('I am a circle.');

	var polygon = L.polygon([
		[51.509, -0.08],
		[51.503, -0.06],
		[51.51, -0.047]
	]).addTo(map).bindPopup('I am a polygon.');


	var popup = L.popup()
		.setLatLng([51.513, -0.09])
		.setContent('I am a standalone popup.')
		.openOn(map);

	function onMapClick(e) {
		popup
			.setLatLng(e.latlng)
			.setContent('You clicked the map at ' + e.latlng.toString())
			.openOn(map);
	}

	map.on('click', onMapClick);
	
/*OpenStreetMap*/	
		


 	
	
	
/*leaf-shadow.png	*/
	

var map = L.map('custom-icons').setView([51.5, -0.09], 13);

	L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(map);

	var LeafIcon = L.Icon.extend({
		options: {
			shadowUrl: 'leaf-shadow.png',
			iconSize:     [38, 95],
			shadowSize:   [50, 64],
			iconAnchor:   [22, 94],
			shadowAnchor: [4, 62],
			popupAnchor:  [-3, -76]
		}
	});

	var greenIcon = new LeafIcon({iconUrl: '../assets/images/icon/leaf-green.png'});
	var redIcon = new LeafIcon({iconUrl: '../assets/images/icon/leaf-red.png'});
	var orangeIcon = new LeafIcon({iconUrl: '../assets/images/icon/leaf-orange.png'});

	var mGreen = L.marker([51.5, -0.09], {icon: greenIcon}).bindPopup('I am a green leaf.').addTo(map);
	var mRed = L.marker([51.495, -0.083], {icon: redIcon}).bindPopup('I am a red leaf.').addTo(map);
	var mOrange = L.marker([51.49, -0.1], {icon: orangeIcon}).bindPopup('I am an orange leaf.').addTo(map);
	
/*leaf-shadow.png	*/	

	
/*layerGroup*/
	var cities = L.layerGroup();

	var mLittleton = L.marker([39.61, -105.02]).bindPopup('This is Littleton, CO.').addTo(cities);
	var mDenver = L.marker([39.74, -104.99]).bindPopup('This is Denver, CO.').addTo(cities);
	var mAurora = L.marker([39.73, -104.8]).bindPopup('This is Aurora, CO.').addTo(cities);
	var mGolden = L.marker([39.77, -105.23]).bindPopup('This is Golden, CO.').addTo(cities);

	var mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery � <a href="https://www.mapbox.com/">Mapbox</a>';
	var mbUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw';

	var grayscale = L.tileLayer(mbUrl, {id: 'mapbox/light-v9', tileSize: 512, zoomOffset: -1, attribution: mbAttr});
	var streets = L.tileLayer(mbUrl, {id: 'mapbox/streets-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr});

	var map = L.map('layerGroup', {
		center: [39.73, -104.99],
		zoom: 10,
		layers: [grayscale, cities]
	});

	var baseLayers = {
		'Grayscale': grayscale,
		'Streets': streets
	};

	var overlays = {
		'Cities': cities
	};

	var layerControl = L.control.layers(baseLayers, overlays).addTo(map);
/*layerGroup*/	


	 
/*wmsLayer*/
var map = L.map('wmsLayer', {
center: [-17, -67],
zoom: 3
});

var wmsLayer = L.tileLayer.wms('http://ows.mundialis.de/services/service?', {
layers: 'TOPO-OSM-WMS'
}).addTo(map);
/*wmsLayer*/	

 
	
	
	
	
	
	
	
	
	