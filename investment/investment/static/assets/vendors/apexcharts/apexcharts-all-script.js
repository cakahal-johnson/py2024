<!--Stacked Area-->
var generateDayWiseTimeSeries = function(baseval, count, yrange) {
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

<!--Stacked Area -->
var ts1 = 1388534400000;
var ts2 = 1388620800000;
var ts3 = 1389052800000;

var dataSet = [
    [],
    [],
    []
];

for (var i = 0; i < 12; i++) {
    ts1 = ts1 + 86400000;
    var innerArr = [ts1, dataSeries[2][i].value];
    dataSet[0].push(innerArr)
}
for (var i = 0; i < 18; i++) {
    ts2 = ts2 + 86400000;
    var innerArr = [ts2, dataSeries[1][i].value];
    dataSet[1].push(innerArr)
}
for (var i = 0; i < 12; i++) {
    ts3 = ts3 + 86400000;
    var innerArr = [ts3, dataSeries[0][i].value];
    dataSet[2].push(innerArr)
} 
<!--Stacked Area-- >


<!--irregular - data - series-- >
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
<!--irregular - data - series-- >


    <!--realtime-- >
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
            x,
            y
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

    for (var i = 0; i < data.length - 10; i++) {
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

function resetData() {
    // Alternatively, you can also reset the data at certain intervals to prevent creating a huge series 
    data = data.slice(data.length - 10, data.length);
}

<!--realtime-- >

<!--Total Transactions-- >
$(function(e) {
    var options = {
        chart: {
            height: 300,
            type: "line",
            foreColor: '#000000',
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
            name: "Total Profit",
            type: 'line',
            data: [0, 45, 30, 75, 15, 94, 40, 115, 30, 105, 65, 110]

        }, {
            name: "Total Orders",
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
                color: 'rgba(0, 0, 0, 1)',
            },
            labels: {
                style: {
                    color: '#2c2c2c',
                    fontSize: '12px',
                },
            },
        },
        yaxis: {
            labels: {
                style: {
                    color: '#2c2c2c',
                    fontSize: '12px',
                },
            },
            axisBorder: {
                show: false,
                foreColor: '#000000',
                color: 'rgba(0, 0, 0, 1)',
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
            show: false,
            foreColor: '#000000'
        },
        legend: {
            position: "top",
            show: true
        }
    }
    var chart = new ApexCharts(document.querySelector("#chartArea"), options);
    chart.render();

});

<!--statistics-- >
$(function(e) {
    'use strict'

    var options = {
        series: [{
            name: 'Average Price',
            data: [44, 42, 57, 86, 58, 55, 70, 52, 29, 56, 75, 61],
            color: ['#664dc9']
        }, {
            name: 'Revenue',
            data: [26, 35, 41, 78, 46, 37, 65, 49, 23, 38, 65, 27]
        }],
        chart: {
            type: 'bar',
            height: 375
        },
        grid: {
            borderColor: '#eff2f6',
        },
        colors: ["#664dc9", '#44c4fa'],
        plotOptions: {
            bar: {
                horizontal: false,
                columnWidth: '30%',
                endingShape: 'rounded'
            },
        },

        dataLabels: {
            enabled: false
        },

        stroke: {
            show: true,
            width: 3,
            colors: ['transparent']
        },
        states: {
            hover: {
                filter: {
                    type: 'none'
                }
            }
        },
        xaxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            axisBorder: {
                show: true,
                color: '#e6ebf1',
                offsetX: 0,
                offsetY: 0,
            },
            axisTicks: {
                show: true,
                borderType: 'solid',
                color: '#e6ebf1',
                width: 6,
                offsetX: 0,
                offsetY: 0
            },
        },
        fill: {
            opacity: 1
        },
        legend: {
            position: "bottom"
        },
    };

    var chart = new ApexCharts(document.querySelector("#statistics"), options);
    chart.render();

    <!--statistics-- >

    <!--spark1-- >
    var spark1 = {
        chart: {
            type: 'area',
            height: 60,
            width: 120,
            sparkline: {
                enabled: true
            },
            dropShadow: {
                enabled: false,
                blur: 3,
                opacity: 0.2,
                show: false,
            }
        },
        stroke: {
            show: true,
            curve: 'smooth',
            lineCap: 'butt',
            colors: ['rgba(255,255,255,0.4)'],
            width: 2,
            dashArray: 0,
        },
        fill: {
            gradient: {
                enabled: false
            }
        },
        series: [{

            name: 'Total Profit',
            data: [0, 80, 50, 32, 54, 21, 64, 30, 30, 38, 60, 50, 34, 40, 31, 26, 90, 50, 60, 25, 52, 41, 20, 45]
        }],
        yaxis: {
            min: 0,
            show: false
        },
        xaxis: {
            axisBorder: {
                show: false
            },
        },
        yaxis: {
            axisBorder: {
                show: false
            },
        },
        colors: ['rgba(255,255,255,0.3)'],

    }
    var spark1 = new ApexCharts(document.querySelector("#spark-charts1"), spark1);
    spark1.render();

    var spark2 = {
        chart: {
            type: 'area',
            height: 60,
            width: 120,
            sparkline: {
                enabled: true
            },
            dropShadow: {
                enabled: false,
                blur: 3,
                opacity: 0.2,
            }
        },
        stroke: {
            show: true,
            curve: 'smooth',
            lineCap: 'butt',
            colors: ['rgba(255,255,255,0.4)'],
            width: 2,
            dashArray: 0,
        },
        fill: {
            gradient: {
                enabled: false
            }
        },
        series: [{
            name: 'Total Orders',
            data: [0, 80, 50, 32, 54, 21, 64, 30, 30, 38, 60, 50, 34, 40, 31, 26, 90, 50, 60, 25, 52, 41, 20, 45]
        }],
        yaxis: {
            min: 0
        },
        colors: ['rgba(255,255,255,0.4)'],

    }
    var spark2 = new ApexCharts(document.querySelector("#spark-charts2"), spark2);
    spark2.render();

    var spark3 = {
        chart: {
            type: 'area',
            height: 60,
            width: 120,
            sparkline: {
                enabled: true
            },
            dropShadow: {
                enabled: false,
                blur: 3,
                opacity: 0.2,
            }
        },
        stroke: {
            show: true,
            curve: 'smooth',
            lineCap: 'butt',
            colors: undefined,
            width: 2,
            dashArray: 0,
        },
        fill: {
            gradient: {
                enabled: false
            }
        },
        series: [{
            name: 'Average Price',
            data: [0, 80, 50, 32, 54, 21, 64, 30, 30, 38, 60, 50, 34, 40, 31, 26, 90, 50, 60, 25, 52, 41, 20, 45]
        }],
        yaxis: {
            min: 0
        },
        colors: ['rgba(255,255,255,0.3)'],

    }
    var spark3 = new ApexCharts(document.querySelector("#spark-charts3"), spark3);
    spark3.render();


    var spark4 = {
        chart: {
            type: 'area',
            height: 60,
            width: 120,
            sparkline: {
                enabled: true
            },
            dropShadow: {
                enabled: false,
                blur: 3,
                opacity: 0.2,
            }
        },
        stroke: {
            show: true,
            curve: 'smooth',
            lineCap: 'butt',
            colors: undefined,
            width: 2,
            dashArray: 0,
        },
        fill: {
            gradient: {
                enabled: false
            }
        },
        series: [{
            name: 'Product Sold',
            data: [0, 80, 50, 32, 54, 21, 64, 30, 30, 38, 60, 50, 34, 40, 31, 26, 90, 50, 60, 25, 52, 41, 20, 45]
        }],
        yaxis: {
            min: 0
        },
        colors: ['rgba(255,255,255,0.3)'],

    }
    var spark4 = new ApexCharts(document.querySelector("#spark-charts4"), spark4);
    spark4.render();


});




/*Performance*/
var options = {
    series: [{
        name: 'This week',
        data: [31, 40, 28, 51, 42, 109, 100]
    }, {
        name: 'Last week',
        data: [11, 32, 45, 32, 34, 52, 41]
    }],

    colors: ['#3734b3', '#75ccff'],
    chart: {
        height: 330,
        type: 'area'
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        curve: 'smooth'
    },
    xaxis: {
        type: 'datetime',
        categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z"]
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    },
};

var chart = new ApexCharts(document.querySelector("#performance"), options);
chart.render();

/*Performance*/


/*Gradient Donut*/
var options = {
    series: [44, 55, 41, 17, 15],
    chart: {
        width: 520,
        type: 'donut',
    },
    plotOptions: {
        pie: {
            startAngle: -90,
            endAngle: 270
        }
    },
    dataLabels: {
        enabled: false
    },
    fill: {
        type: 'gradient',
    },
    legend: {
        formatter: function(val, opts) {
            return val + " - " + opts.w.globals.series[opts.seriesIndex]
        }
    },
    responsive: [{
        breakpoint: 480,
        options: {
            chart: {
                width: 200
            },
            legend: {
                position: 'bottom'
            }
        }
    }]
};

var chart = new ApexCharts(document.querySelector("#gradient-donut"), options);
chart.render();
/*Gradient Donut*/