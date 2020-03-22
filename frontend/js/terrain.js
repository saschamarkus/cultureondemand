console.info('Welcome to Culture On Demand.');
console.info('=============================');

const width = 600;
    const yScale = d3.scaleLinear().domain([0, 1200]).range([600, 0]);

let m = 11;

let x = d3.scaleLinear([0, m - 1], [0, width]);

let areaGenerator = d3.area()
    .x(function (d, i) {
        return x(i)
    })
    .y0(function (d) {
        return yScale(d[0]);
    })
    .y1(function (d) {
        return yScale(d[1]);
    });

let colors = ['#009be0', '#05991b', '#ffe600', '#ef7a1d', '#e42a4b', '#bd077f', '#332881'];

let data = [
    {ueberrascht: 0, gluecklich: 0, traurig: 0, angewidert: 0, wuetend: 0, aengstlich: 0, schlecht: 0},
    {ueberrascht: 150, gluecklich: 50, traurig: 0, angewidert: 50, wuetend: 0, aengstlich: 0, schlecht: 0},
    {ueberrascht: 150, gluecklich: 100, traurig: 0, angewidert: 100, wuetend: 50, aengstlich: 0, schlecht: 0},
    {ueberrascht: 100, gluecklich: 150, traurig: 0, angewidert: 250, wuetend: 150, aengstlich: 0, schlecht: 0},
    {ueberrascht: 150, gluecklich: 200, traurig: 0, angewidert: 300, wuetend: 200, aengstlich: 0, schlecht: 0},
    {ueberrascht: 100, gluecklich: 250, traurig: 0, angewidert: 350, wuetend: 250, aengstlich: 0, schlecht: 0},
    {ueberrascht: 200, gluecklich: 270, traurig: 0, angewidert: 350, wuetend: 220, aengstlich: 0, schlecht: 0},
    {ueberrascht: 200, gluecklich: 300, traurig: 0, angewidert: 320, wuetend: 150, aengstlich: 0, schlecht: 0},
    {ueberrascht: 250, gluecklich: 330, traurig: 0, angewidert: 300, wuetend: 0, aengstlich: 0, schlecht: 150},
    {ueberrascht: 200, gluecklich: 350, traurig: 0, angewidert: 270, wuetend: 0, aengstlich: 0, schlecht: 160},
    {ueberrascht: 150, gluecklich: 330, traurig: 200, angewidert: 250, wuetend: 50, aengstlich: 0, schlecht: 170},
    {ueberrascht: 190, gluecklich: 300, traurig: 250, angewidert: 200, wuetend: 100, aengstlich: 0, schlecht: 160},
    {ueberrascht: 200, gluecklich: 300, traurig: 200, angewidert: 150, wuetend: 150, aengstlich: 50, schlecht: 150},
    {ueberrascht: 150, gluecklich: 250, traurig: 210, angewidert: 100, wuetend: 200, aengstlich: 100, schlecht: 100},
    {ueberrascht: 100, gluecklich: 200, traurig: 220, angewidert: 50, wuetend: 250, aengstlich: 150, schlecht: 50},
    {ueberrascht: 80, gluecklich: 200, traurig: 200, angewidert: 0, wuetend: 300, aengstlich: 200, schlecht: 100},
    {ueberrascht: 60, gluecklich: 150, traurig: 250, angewidert: 0, wuetend: 250, aengstlich: 150, schlecht: 150},
    {ueberrascht: 50, gluecklich: 100, traurig: 200, angewidert: 0, wuetend: 150, aengstlich: 0, schlecht: 200},
    {ueberrascht: 30, gluecklich: 50, traurig: 150, angewidert: 0, wuetend: 0, aengstlich: 0, schlecht: 250},
    {ueberrascht: 0, gluecklich: 0, traurig: 0, angewidert: 0, wuetend: 0, aengstlich: 0, schlecht: 300}
];

let stack = d3.stack()
    .keys([
        'ueberrascht',
        'gluecklich',
        'traurig',
        'angewidert',
        'wuetend',
        'aengstlich',
        'schlecht'
    ]);

let stackedSeries = stack(data);

d3.select('g')
    .selectAll('path')
    .data(stackedSeries)
    .enter()
    .append('path')
    .style('fill', function (d, i) {
        return colors[i];
    })
    .attr('d', areaGenerator)
    .on("mouseover", function (d) {
        d3.select(this).transition()
            .duration(200)
            .style("opacity", .8);
    })
    .on("mouseout", function (d) {
        d3.select(this).transition()
            .duration(500)
            .style("opacity", 1);
    });

// Define the div for the tooltip
let div = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

d3.json('http://localhost:8888/data/results.json').then((data) => {
    console.info(data);
    let trianglePoints = [5, 30, 15, 10, 25, 30];

    d3.select('svg')
        .selectAll("polyline")
        .data(data)
        .enter()
        .append("polyline")
        .attr('points', trianglePoints)
        .attr("transform", function (d) {
            return "translate(" + d.x + "," + d.y + ")";
        })
        .style("fill", "black")
        .on("mouseover", function (d) {
            div.transition()
                .duration(200)
                .style("opacity", .9);
            div.html('<b>Emotion:</b> ' + d.emotion + '<br>' +
                '<b>Erfahrung:</b> ' + d.experience + '<br>' +
                '<b>Interaktion:</b> ' + d.interactivity + '<br>' +
                '<b>Medium:</b> ' + d.media)
                .style("left", (d3.event.pageX) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
        })
        .on("mouseout", function (d) {
            div.transition()
                .duration(500)
                .style("opacity", 0);
        });
});
