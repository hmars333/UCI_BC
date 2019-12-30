function buildMetadata(sample) {

// Step 1: Plotly
// 1. Use the D3 library to read in `samples.json`.
d3.json('samples.json').then((data)=> {
    var metadata= data.metadata;
//filter to get sample ID's/ sample number
    var results= metadata.filter(sampleObj => sampleObj.id == sample);
    var result1= results[0];
    var Panel= d3.select("#sample-metadata");
//clear existing Metadata
    Panel.html("");

    Object.entries(result1).forEach(([key, value]) => {
        Panel.append("h6").text(`${key.toUpperCase()}: ${value}`);

    });
});
}

// 2. Create a horizontal bar chart with a dropdown menu to display the top 10 OTUs found in that individual.
function buildCharts(sample){

// * Use `sample_values` as the values for the bar chart.
// * Use `otu_ids` as the labels for the bar chart.
// * Use `otu_labels` as the hovertext for the chart.
d3.json('samples.json').then((data)=> {
    var samples= data.samples;
    var results= samples.filter(sampleObj=> sampleObj.id == sample);
    var result1 = results[0];
    var sample_values= result1.sample_values;
    var otu_ids= result1.otu_ids;
    var otu_labels= result1.otu_labels;
    console.log("sample values:", sample_values, "otu IDs:", otu_ids, "otu Labels:", otu_labels);

//bubble chart//
    var bubbleLayout = {
        title: "Bacteria Cultures Per Sample",
        margin: { t: 0},
        hovermode: "closest",
        xaxis: {title: "OTU ID" },
        margin: {t: 30}
    };
    var bubbleData = [{
        x:  otu_ids,
        y: sample_values,
        text: otu_labels,
        mode: "markers",
        marker: {
            size: sample_values,
            color: otu_ids,
            colorscale: "Electric"
        }

    }];
    Plotly.newPlot("bubble", bubbleData, bubbleLayout);
//bar chart//
var yticks= otu_ids.slice(0,10).map(otuID => `OTU ${otuID}`).reverse();
var barData= [{
    y: yticks,
    x: sample_values.slice(0,10).reverse(),
    text: otu_labels.slice(0,10).reverse(),
    orientation: 'h',
    type: 'bar'
}];

var barLayout = {
    title: "Top 10 Bacteria Cultures Found",
    margin: {t: 50, l: 150}
};

Plotly.newPlot("bar", barData, barLayout);

});

} 
 //dropdown menu//
 function init(){
     var selector= d3.select("#selDataset");
     d3.json("samples.json").then((data) => {
         var sampleNames= data.names;
         sampleNames.forEach((sample) => {
             selector
             .append("option")
             .text(sample)
             .property("value", sample);

         });
//first chart sample
         var firstSample= sampleNames[0];
         buildCharts(firstSample);
         buildMetadata(firstSample);
     });
 }

 //new sample
 function optionChanged(newSample) {
     buildCharts(newSample);
     buildMetadata(newSample);

 }
 init();
