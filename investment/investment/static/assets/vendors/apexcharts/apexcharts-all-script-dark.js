
<!--Stacked Area-->

    var generateDayWiseTimeSeries = function (baseval, count, yrange) {
      var i = 0;
      var series = [];
      while (i < count) {
        var x = baseval;
        var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
  
        series.push([x, y]);
        baseval += 86400000;
        i++;
      }
      return series;
	  
    }
 
<!--Stacked Area-->
var ts1 = 1388534400000;
var ts2 = 1388620800000;
var ts3 = 1389052800000;

var dataSet = [[],[],[]];

for(var i=0; i<12; i++) {
ts1 = ts1 + 86400000;
var innerArr = [ts1, dataSeries[2][i].value];
dataSet[0].push(innerArr)
}
for(var i=0; i<18; i++) {
ts2 = ts2 + 86400000;
var innerArr = [ts2, dataSeries[1][i].value];
dataSet[1].push(innerArr)
}
for(var i=0; i<12; i++) {
ts3 = ts3 + 86400000;
var innerArr = [ts3, dataSeries[0][i].value];
dataSet[2].push(innerArr)
}
<!--Stacked Area-->


<!--irregular-data-series-->
var options = {
series: [{
name: 'PRODUCT A',
data: dataSet[0]
}, {
name: 'PRODUCT B',
data: dataSet[1]
}, {
name: 'PRODUCT C',
data: dataSet[2]
}],
chart: {
type: 'area',
stacked: false,
height: 350,
foreColor:'#ffffff',
zoom: {
enabled: false
},
},
dataLabels: {
enabled: false
},
markers: {
size: 0,
},
fill: {
type: 'gradient',
gradient: {
  shadeIntensity: 1,
  inverseColors: false,
  opacityFrom: 0.45,
  opacityTo: 0.05,
  stops: [20, 100, 100, 100]
},
},
yaxis: {
labels: {
  style: {
      colors: '#8e8da4',
  },
  offsetX: 0,
  formatter: function(val) {
    return (val / 1000000).toFixed(2);
  },
},
axisBorder: {
  show: false,
},
axisTicks: {
  show: false
}
},
xaxis: {
type: 'datetime',
tickAmount: 8,
min: new Date("01/01/2014").getTime(),
max: new Date("01/20/2014").getTime(),
labels: {
  rotate: -15,
  rotateAlways: true,
  formatter: function(val, timestamp) {
    return moment(new Date(timestamp)).format("DD MMM YYYY")
}
}
},
title: {
text: 'Irregular Data in Time Series',
align: 'left',
offsetX: 14
},
tooltip: {
shared: true
},
legend: {
position: 'top',
horizontalAlign: 'right',
offsetX: -10
}
};

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();
<!--irregular-data-series-->


<!--realtime-->
var lastDate = 0;
var data = []
var TICKINTERVAL = 86400000
let XAXISRANGE = 777600000
function getDayWiseTimeSeries(baseval, count, yrange) {
var i = 0;
while (i < count) {
var x = baseval;
var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

data.push({
x, y
});
lastDate = baseval
baseval += TICKINTERVAL;
i++;
}
}

getDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 10, {
min: 10,
max: 90
})

function getNewSeries(baseval, yrange) {
var newDate = baseval + TICKINTERVAL;
lastDate = newDate

for(var i = 0; i< data.length - 10; i++) {
// IMPORTANT
// we reset the x and y of the data which is out of drawing area
// to prevent memory leaks
data[i].x = newDate - XAXISRANGE - TICKINTERVAL
data[i].y = 0
}

data.push({
x: newDate,
y: Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min
})
}

function resetData(){
// Alternatively, you can also reset the data at certain intervals to prevent creating a huge series 
data = data.slice(data.length - 10, data.length);
}

<!--realtime-->	


<!--Total Transactions-->
$(function(e) {

    /*-----echart1-----*/
	var options = {
		chart: {
			height: 300,
			type: "line",
			foreColor: '#e7e7e7',
			stacked: false,
			toolbar: {
				enabled: false
			},
			dropShadow: {
				enabled: true,
				opacity: 0.1,
			},
		},
		colors: ["#57c9c9", "#d92642", 'rgba(255, 255, 255, 0.05)'],
		dataLabels: {
			enabled: false
		},
		stroke: {
			curve: "smooth",
			width: [3, 3, 0],
			dashArray: [0, 4],
			lineCap: "round"
		},
		grid: {
			padding: {
				left: 0,
				right: 0
			},
			strokeDashArray: 3
		},
		markers: {
			size: 0,
			hover: {
				size: 0
			}
		},
		series: [{
			name: "Total Orders",
			type: 'line',
			data: [0, 45, 30, 75, 15, 94, 40, 115, 30, 105, 65, 110]
			
		},{
			name: "Total Sales",
			type: 'line',
			data: [0, 60, 20, 130, 75, 130, 75, 140, 64, 130, 85, 120]
		}, {
			name: "",
			type: 'area',
			data: [0, 105, 70, 175, 85, 154, 90, 185, 120, 145, 185, 130]
		}],
		xaxis: {
			type: "month",
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
			axisBorder: {
				show: false,
				color: 'rgba(255, 255, 255, 1)',
			},
			labels: {
				style: {
					color: '#FFFFFF',
					fontSize: '12px',
				},
			},
		},
		yaxis: {
			labels: {
				style: {
					color: '#FFFFFF',
					fontSize: '12px',
				},
			},
			axisBorder: {
				show: false,
				color: 'rgba(255, 255, 255, 1)',
			},
		},
		fill: {
			gradient: {
			  inverseColors: false,
			  shade: 'light',
			  type: "vertical",
			  opacityFrom: 0.85,
			  opacityTo: 0.55,
			  stops: [0, 100, 100, 100]
			}
		  },
		tooltip: {
			show:false
		},
		legend: {
			position: "top",
			show:true
		}
	}
	var chart = new ApexCharts(document.querySelector("#chartArea"), options);
	chart.render();
	
 });
 
<!--Total Transactions-->