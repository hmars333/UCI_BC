var samples= d3.json("./samples.json").then(function(sampleData){
    console.log(sampleData);
})

var oTU= samples.samples.otu_ids;
var otuValues= samples.samples.sample_values;
var otuIndiv= samples.names;


forEach indiv in otuIndiv
function topTen(OTUs) {
    return otuValues.slice(0,11), 
  }
  
