$(function(){
    // chart
    // data array
    var d1 = [];
    for (var i = 0; i < 14; i += 0.5)
        d1.push([i, Math.sin(i)]);

    var d2 = [[0, 3], [4, 8], [8, 5], [9, 13]];

    var d3 = [];
    for (var i = 0; i < 14; i += 0.5)
        d3.push([i, Math.cos(i)]);

    var d4 = [];
    for (var i = 0; i < 14; i += 0.1)
        d4.push([i, Math.sqrt(i * 10)]);

    var d5 = [];
    for (var i = 0; i < 14; i += 0.5)
        d5.push([i, Math.sqrt(i)]);

    var d6 = [];
    for (var i = 0; i < 14; i += 0.5 + Math.random())
        d6.push([i, Math.sqrt(2*i + Math.sin(i) + 5)]);
                
    var d7 = [];
    for (var i = 0; i <= 10; i += 1)
        d7.push([i, parseInt(Math.random() * 30)]);

    var d8 = [];
    for (var i = 0; i <= 10; i += 1)
        d8.push([i, parseInt(Math.random() * 30)]);

    var d9 = [];
    for (var i = 0; i <= 10; i += 1)
        d9.push([i, parseInt(Math.random() * 30)]);

                
    // variable lines
    var lines = $("#chart-lines"),
    data_lines = [{
        label: 'data 1', 
        data: d1,
        color: '#008299'
    }, {
        label: 'data 2', 
        data: d2,
        color: '#D24726'
    }, {
        label: 'data 3', 
        data: d3,
        color: '#8C0095'
    }],
    options_lines = {
        series: {
            lines: {
                show: true
            },
            points: {
                show: true
            },
            hoverable: true
        },
        grid: {
            backgroundColor: '#FFFFFF', // you can use gradiend like this { colors: [ "#FFFFFF", "#F1F1F1" ] }
            borderWidth: 1,
            borderColor: '#D7D7D7',
            hoverable: true, 
            clickable: true
        }
                        
    };
    // rendering plot lines
    var chart_lines = $.plot(lines, data_lines, options_lines);
                
                
    // variable points
    var points = $("#chart-points"),
    data_points = [{
        label: 'data 1', 
        data: d3, 
        points:{
            symbol: "cross"
        },
        color: '#AC193D'
    }, {
        label: 'data 2', 
        data: d4, 
        points:{
            symbol: "square"
        },
        color: '#D24726'
    }, {
        label: 'data 3', 
        data: d5, 
        points:{
            symbol: "diamond"
        },
        color: '#008A00'
    }, {
        label: 'data 4', 
        data: d2, 
        points:{
            symbol: "triangle"
        },
        color: '#094AB2'
    }],
    options_points = {
        series: {
            points: {
                show: true
            }
        },
        grid: {
            backgroundColor: '#FFFFFF',
            borderWidth: 1,
            borderColor: '#D7D7D7'
        }
    };
    // rendering plot points
    var chart_points = $.plot(points, data_points, options_points);
    
                
    // variable filled
    var filled = $("#chart-filled"),
    data_filled = [{
        label: 'data 1', 
        data: d6,
        color: '#2672EC'
    }, {
        label: 'data 2', 
        data: d5,
        color: '#AC193D'
    }, {
        label: 'data 3', 
        data: d3,
        color: '#008A00'
    }],
    options_filled = {
        series: {
            lines: {
                show: true, 
                fill: true
            },
            points: {
                show: true
            },
            hoverable: true
        },
        grid: {
            backgroundColor: '#FFFFFF',
            borderWidth: 1,
            borderColor: '#D7D7D7',
            hoverable: true, 
            clickable: true
        }
    };
    // rendering plot filled
    var chart_filled = $.plot(filled, data_filled, options_filled)
    function showTooltip(x, y, contents) {
        $('<div id="tooltip" class="bg-black corner-all color-white">' + contents + '</div>').css( {
            position: 'absolute',
            display: 'none',
            top: y + 5,
            left: x + 5,
            border: '0px',
            padding: '2px 10px 2px 10px',
            opacity: 0.9,
            'font-size' : '11px'
        }).appendTo("body").fadeIn(200);
    }
    $(filled).bind("plothover", function (event, pos, item) {
        if (item) {
            if (previousPoint != item.dataIndex) {
                previousPoint = item.dataIndex;

                $("#tooltip").remove();
                var x = item.datapoint[0].toFixed(2),
                y = item.datapoint[1].toFixed(2);
                
                showTooltip(item.pageX, item.pageY,
                item.series.label + " of " + x + " = " + y);
                
            }
        }
        else {
            $("#tooltip").remove();
            previousPoint = null;            
        }
    });
                
    // variable bars
    var bars = $("#chart-bars"),
    data_bars = [{
        data : [ ["January", 10], ["February", 8], ["March", 4], ["April", 13], ["May", 17], ["June", 9] ],
        color: '#AC193D'
    }];
    options_bars = {
        series: {
            bars: {
                show: true,
                barWidth: 0.6,
                align: "center"
            }
        },
        xaxis: {
            mode: "categories",
            tickLength: 0
        },
        crosshair: {
            mode: "xy",
            color: "#D24726"
        },
        grid: {
            backgroundColor: '#FFFFFF',
            borderWidth: 1,
            borderColor: '#D7D7D7',
            hoverable: true
        }
    };
    // rendering plot bars
    var chart_bars = $.plot(bars, data_bars, options_bars);
                
                
    // variable stacking
    var stacking = $("#chart-stacking"),
    data_stacking = [{
        label: 'data 1', 
        data: d7,
        color: '#008A00'
    }, {
        label: 'data 2', 
        data: d8,
        color: '#5133AB'
    }, {
        label: 'data 3', 
        data: d9,
        color: '#2672EC'
    }],
    stack = 0, bars = true, lines = false, steps = false;
    // rendering plot stacking
    function plotWithOptions() {
        $.plot(stacking, data_stacking, {
            series: {
                stack: stack,
                lines: {
                    show: lines, 
                    fill: true, 
                    steps: steps
                },
                bars: {
                    show: bars, 
                    barWidth: 0.6
                }
            },
            grid: {
                backgroundColor: '#FFFFFF',
                borderWidth: 1,
                borderColor: '#D7D7D7',
                hoverable: true, 
                clickable: true
            }
        })
    }
                
    plotWithOptions();
                
    $(".stackControls input").click(function (e) {
        e.preventDefault();
        stack = $(this).val() == "With stacking" ? true : null;
        plotWithOptions();
    });
    $(".graphControls input").click(function (e) {
        e.preventDefault();
        bars = $(this).val().indexOf("Bars") != -1;
        lines = $(this).val().indexOf("Lines") != -1;
        steps = $(this).val().indexOf("steps") != -1;
        plotWithOptions();
    });
                
    // variable pie
    var pie1 = $("#chart-pie1"),
    pie2 = $("#chart-pie2"),
    pie3 = $("#chart-pie3"),
    data_pie = [],
    series = Math.floor(Math.random()*6)+3;
    for( var i = 0; i<series; i++){
            data_pie[i] = { label: "Series"+(i+1), data: Math.floor(Math.random()*100)+1 }
    }
    options_pie1 = {
        series: {
            pie: { 
                show: true
            }
        },
        grid: {
            backgroundColor: '#FFFFFF',
            borderWidth: 1,
            borderColor: '#D7D7D7',
            hoverable: true,
            clickable: true
        }
    };
    options_pie2 = {
        series: {
            pie: { 
                show: true
            }
        },
        grid: {
            backgroundColor: '#FFFFFF',
            borderWidth: 1,
            borderColor: '#D7D7D7',
            hoverable: true,
            clickable: true
        },
        legend: {
            show: false
        }
    };
    options_pie3 = {
        series: {
            pie: {
                show: true,
                radius: 1,
                tilt: 0.5,
                label: {
                    show: true,
                    radius: 1,
                    formatter: function(label, series){
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'+label+'<br/>'+Math.round(series.percent)+'%</div>';
                    },
                    background: { opacity: 0.8 }
                },
                combine: {
                    color: '#999',
                    threshold: 0.1
                }
            }
        },
        grid: {
            backgroundColor: '#FFFFFF',
            borderWidth: 1,
            borderColor: '#D7D7D7',
            hoverable: true,
            clickable: true
        },
        legend: {
            show: false
        }
    };
    // rendering plot pie
    $.plot(pie1, data_pie, options_pie1);
    $.plot(pie2, data_pie, options_pie2);
    $.plot(pie3, data_pie, options_pie3);
          
    // variable ajax
    var ajax = $("#chart-ajax"),
    data_ajax = [],
    alreadyFetched = {},
    options_ajax = {
        series: {
            lines: {
                show: true
            },
            points: {
                show: true
            },
            hoverable: true
        },
        xaxis: {
            mode: "categories",
            tickLength: 0
        },
        grid: {
            backgroundColor: '#FFFFFF', // you can use gradiend like this { colors: [ "#FFFFFF", "#F1F1F1" ] }
            borderWidth: 1,
            borderColor: '#D7D7D7',
            hoverable: true, 
            clickable: true
        }

    };
    // then fetch the data with jQuery
    function onDataReceived(series) {
        // let's add it to our current data
        if (!alreadyFetched[series.label]) {
            $.each(series, function(i, v){
                alreadyFetched[series.label] = true;
                data_ajax.push(series[i]);
            })
        }

        // and plot all we got
        $.plot(ajax, data_ajax, options_ajax);
    }

    $.ajax({
        url: 'js/flot/data-usa-gdp-growth.json',
        type: 'GET',
        dataType: 'json',
        success: onDataReceived
    });

    // variable realtime
    var data = [], totalPoints = 300;
    function getRandomData() {
        if (data.length > 0)
            data = data.slice(1);

        // do a random walk
        while (data.length < totalPoints) {
            var prev = data.length > 0 ? data[data.length - 1] : 50;
            var y = prev + Math.random() * 10 - 5;
            if (y < 20)
                y = 20;
            if (y > 80)
                y = 80;
            data.push(y);
        }

        // zip the generated y values with the x values
        var res = [];
        for (var i = 0; i < data.length; ++i)
            res.push([i, data[i]])
        return res;
    };
    var updateInterval = 30; // this max value recomended to 2000
    var realtime = $("#chart-realtime"),
    data_realtime = [getRandomData()];
    options_realtime = {
        series: {
            lines: {
                show: true
            }
        },
        grid: {
            backgroundColor: '#FFFFFF',
            borderWidth: 1,
            borderColor: '#D7D7D7'
        }
    };
    // rendering plot realtime
    var chart_realtime = $.plot(realtime, data_realtime, options_realtime);
    // re-rendering by interval
    function update() {
        chart_realtime.setData([ {data: getRandomData(), color: '#00CCFF'} ]);
        // since the axes don't change, we don't need to call plot.setupGrid()
        chart_realtime.draw();

        setTimeout(update, updateInterval);
    }

    update();

})