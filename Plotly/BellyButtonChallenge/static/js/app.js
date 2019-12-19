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
    
  })
}


// var oTU= samples.samples.otu_ids;
// console.log(oTU);
// var otuValues= samples.samples.sample_values;
// console.log(otuValues);
// var otuIndiv= samples.names;
// console.log(otuIndiv);


// sampleData.forEach(function(data){
//   return sampleData.slice(0,11);
// })

