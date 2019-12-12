// from data.js
var tableData = data;

// YOUR CODE HERE!
var tbody= d3.select("tbody");

function buildTable(data) {
    tbody.html(" ");
    data.forEach((dataRow) => {
        var row= tbody.append("tr");
        Object.values(dataRow).forEach((val) => {
            var cell= row.append("td");
            cell.text(val);
        }
        );
    });
}


function clicks() {
    var date= d3.select("#datetime").property("value");
    let filterData= tableData;
    if (date) {
        filterData =filterData.filter(row => row.datetime=== date);

    }
    buildTable(filterData);
}

d3.selectAll("#filter-btn").on ("click", clicks);

buildTable(tableData);
