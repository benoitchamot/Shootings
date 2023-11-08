function displayGauge(value) {
// Display gauge
    
    let data = [
        {
            domain: { x: [0, 1], y: [0, 1] },
            value: value,
            title: { text: "Risk Factor" },
            type: "indicator",
            mode: "gauge+number",
            gauge: {
                bar: {
                    color: "black"
                },
                axis:{range: [0, 3000], type:"log"},
                steps: [
                { range: [0, 10], color: "#548235" },
                { range: [10, 100], color: "#F4B183" },
                { range: [100, 1000], color: "#ED7D31" },
                { range: [1000, 3000], color: "#a52a2a"}
                ],
                threshold: {
                line: {'color': "black", 'width': 2},
                thickness: 0.75,
                value: value}
            }
        }
    ];
        
    // Render the gauge to the div tag with id "gauge"
    Plotly.newPlot('gauge', data);
}