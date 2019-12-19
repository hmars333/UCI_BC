function data(sample){
  d3.json("../samples.json").then((sampleData) => {
    var metaData= sampleData.metadata;
    var results= metaData.filter(sampleObj.id == sample);
    var result = results[0];
    var panel= d3.select("#sample-metadata");
  
    Object.entries(result).forEach(([key, value]) => {
      panel.append("h6").text(`${key.toUppercase()}: ${value}`);
    });
  
  });  
  
}

function charts(sample){

  d3.json("../samples.json").then((sampleData) => {
    var samples= sampleData.samples;
    var results= samples.filter(sampleObj => sampleObj.id== sample);
    var result =results[0];
    var otu_ids= result.otu_ids;
    var otu_labels= result.otu_labels;
    var sample_values= result.sample_values;


    var bubbleLayout= {
      title: "Bacteria Per Sample",
      margin: {t: 50},
      hovermode: "closest",
      xaxis: { title: "OTU ID" },
      margin: {t: 50},
    };

    var bubbleData = [
      {
        x: otu_ids,
        y: sample_values,
        text: otu_labels,
        mode: "markers",
        marker: {
          size: sample_values,
          color: otu_ids,
          colorscale: "Earth"
        }

    }
  ];
Plotly.newPlot("bubble", bubbleData, bubbleLayout);

var yticks= otu_ids.slice(0,10).map(otuID => `OTU ${otuID}`).reverse();
var barChart=[
  {
    y: yticks,
    x: sample_values.slice(0,10).reverse(),
    text: otu_labels.slice(0, 10).reverse(),
    type: "bar",
    orientation: "h",   
  }
];

var layout= {
  title: "Top 10 Most Common Bacteria",
  margin: { l: 50, r: 50}
};

Plotly.newPlot("bar", barChart, layout);
  });
}

function init() {
  var selector = d3.select("#selDataset"); 
  
  d3.json("../samples.json").then((sampleData) => {
    var sampleNames = sampleData.names;
    sampleNames.forEach((sample) => {
      selector.append("option")
      .text(sample)
      .property("value", sample);
    });

    var firstSample= sampleNames[0];
    buildCharts(firstSample);
    buildData(firstSample);  
  });
}

function optionChange(newSample) {
  buildCharts(newSample);
  buildData(newSample);
}

init();