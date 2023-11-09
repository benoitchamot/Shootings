function displayGauge(value) {

    let section = d3.select('#gauge')
    section.html("")

    // create data
    var data = [value];
 
    // set the gauge type
    var gauge = anychart.gauges.linear();
 
    // set the data for the gauge
    gauge.data(data);
 
    // set the layout
    gauge.layout('horizontal');
 
    // create a color scale
    var scaleBarColorScale = anychart.scales.ordinalColor().ranges(
    [
        {
            from: 0,
            to: 10,
            color: ['#2AD62A', '#CAD70b']
        },
        {
            from: 10,
            to: 100,
            
            color: ['#CAD70b', '#FFD700']
        },
        {
            from: 100,
            to: 1000,
            color: ['#FFD700', '#EB7A02']
        },
        {
            from: 1000,
            to: 3000,
            
            color: ['#EB7A02', '#D81E05']
        }
    ]
    );
 
    // create a Scale Bar
    var scaleBar = gauge.scaleBar(0);
 
    // set the height and offset of the Scale Bar (both as percentages of the gauge height)
    scaleBar.width('25%');
    scaleBar.offset('15%');
 
    // use the color scale (defined earlier) as the color scale of the Scale Bar
    scaleBar.colorScale(scaleBarColorScale);
 
    // add a marker pointer
    var marker = gauge.marker(0);
 
    // set the offset of the pointer as a percentage of the gauge width
    marker.offset('-6%');
 
    // set the marker type
    marker.type('triangle-down');
 
    // set the zIndex of the marker
    marker.zIndex(10);
    marker.color('#c3c3c3');
    marker.width(20);
 
    // configure the scale
    var scale = gauge.scale();
    scale.minimum(0);
    scale.maximum(3000);
    scale.ticks().interval(100);
 
    // configure the axis
    var axis = gauge.axis();
    axis.minorTicks(true)
    axis.minorTicks().stroke('#cecece');
    axis.width('1%');
    axis.offset('45.5%');
    axis.orientation('bottom');
 
    // format axis labels
    axis.labels().format('{%value}');
 
    // set paddings
    gauge.padding([10, 50]);
 
    // set the container id
    gauge.container('gauge');
 
    // initiate drawing the gauge
    gauge.draw();
}
