var svgWidth = 1000
var svgHeight= 700

var Margin= {
  top: 25,
  right: 25,
  bottom: 25,
  left:25
};

var chartWidth= svgWidth -Margin.left -Margin.right;
var chartHeight= svgHeight-Margin.top-Margin.bottom;


var svg= d3.select("body")
.append(svg)
.attr("height", svgHeight)
.attr("width", svgWidth);

var chartGroup = svg.append("g")
.attr("tranform", `translate(${Margin.left}, ${Margin.top})`);


d3.json("samples.json", function(sampleData){
  console.log(sampleData);
})

sampleData.forEach(function(data){
  data.id= sampleData.sampleData.otu_ids
});

otuIDs= data.id.slice(0,11);
console.log(otuIDs);

var xScale= d3.scaleBand()
.domain(sampleData.map(data => data.names)
.range([0,chartWidth])
.padding(0.5));

var yScale= d3.scaleLinear()
.domain([0, d3.Max(sampleData, data => data.id)])
.range([chartHeight,0]);


var bottomAxis= d3.axisBottom(xScale);
var leftAxis= d3.axisLeft(yScale);


chartGroup.append("g")
.call(leftAxis);

chartGroup.append("g")
.attr("transform", `translate (0, ${chartHeight})`)
.call(bottomAxis);

chartGroup.selectAll(".bar")
.data(sampleData)
.append("rect")
.attr("class", "bar")
.attr("x", )












// var oTU= samples.samples.otu_ids;
// console.log(oTU);
// var otuValues= samples.samples.sample_values;
// console.log(otuValues);
// var otuIndiv= samples.names;
// console.log(otuIndiv);


// sampleData.forEach(function(data){
//   return sampleData.slice(0,11);
// })

