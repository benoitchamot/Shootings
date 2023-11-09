// Global variables
let n_rows = 0

// Clear table
function clearTable() {

    // Deleyte rows in database
    // Get classification and probability
    delete_url = 'http://127.0.0.1:5000/api/v1.0/blackbox/clear';
    d3.json(delete_url).then(function(error) {
        if (error=="0") {
            alert('Entries deleted');
        } else {
            alert(error);
        }
    }).then(updateCount);

    // Delete rows in HTML
    let table = $("#csvtable > tbody");
    table.empty();
    n_rows = 0;
}

function displayRisk(data) {
    // Select current row
    console.log(data.Classification);
    console.log(data.Probability);
}

function updateHTMLTable(data) {
    console.log('Data received')
    let table = $("#csvtable > tbody");

    // Delete rows in HTML
    table.empty();

    // Define color scale for probability
    function setColor(value) {
        let color = "white"

        if (value) {
            if (value<30) {
                color = "green"
                console.log(value);
            } else if (value <70) {
                color = "orange"
                console.log(value);
            } else {
                color = "red"
                console.log(value);
            }    
        } 
        return color;
    }
    
    // Format number
    let formatPercent = d3.format(".1f");

    // Loop through the data
    for (let i = 0; i<data.length; i++) {

        if (data[i] != "") {  
            let row = "<tr>"
                    + "<td>" + data[i].Age + "</td>"
                    + "<td>" + data[i].Gender + "</td>"
                    + "<td>" + data[i].Race + "</td>"
                    + "<td>" + data[i].Immigrant + "</td>"
                    + "<td>" + data[i].Education + "</td>"
                    + "<td>" + data[i].RelStatus + "</td>"
                    + "<td>" + data[i].Employed + "</td>"
                    + "<td>" + data[i].Work + "</td>"
                    + "<td>" + data[i].MilService + "</td>"
                    + "<td>" + data[i].Arrested + "</td>"
                    + "<td>" + data[i].ParentDivorce + "</td>"
                    + "<td>" + data[i].SES + "</td>"
                    + "<td>" + data[i].MentalIllness + "</td>"
                    + "<td>" + data[i].MentalIllnessHistory + "</td>"
                    + "<td>" + data[i].Autism + "</td>"
                    + "<td>" + data[i].HealthIssues + "</td>"
                    + "<td>" + data[i].Classification + "</td>"
                    + "<td style='color:" + setColor(data[i].Probability) +"'>" + formatPercent(data[i].Probability) + "%</td>"
                    + "</tr>"; 
                
                // Add row to table
                table.append(row);  
        }  
    }

    // Update HTML table
    $('#csvtable').show();  
}


// Update the entry counter
function updateCount() {
    let count_url = 'http://127.0.0.1:5000/api/v1.0/blackbox/count'
    d3.json(count_url).then(function(data) {
        console.log(data);
        d3.select('#database_entry_count').text(`Total entries: ${data}`);
    });
}


// Retrieve data from database and display it in HTML table
function updateFromDatabase() {
    // Get data from API
    get_url = 'http://127.0.0.1:5000/api/v1.0/blackbox/get';
    d3.json(get_url).then(updateHTMLTable);

}

function identify() {
    
    // Send request to run identification on data in database
    let identify_url = 'http://127.0.0.1:5000/api/v1.0/blackbox/identify';
    d3.json(identify_url).then(updateHTMLTable).then(function() {
        // Alert the user that data are ready
        alert("Analysis completed.")
    });
}

// Source: https://www.c-sharpcorner.com/blogs/reading-a-csv-file-using-html5-jquery
function upload() {  
    var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv)$/;  
    //Checks whether the file is a valid csv file    
    if (regex.test($("#csvfile").val().toLowerCase())) {
        //Checks whether the browser supports HTML5    
        if (typeof(FileReader) != "undefined") {  
            var reader = new FileReader();  
            reader.onload = function(e) {  
            var table = $("#csvtable > tbody");
       
            //Splitting of Rows in the csv file    
            var csvrows = e.target.result.split("\n");
            n_rows += csvrows.length-1;
            
            // Start loading rows from the second row (skip header)
            for (var i = 1; i < csvrows.length; i++) {
                    // Split rows on commas
                    var csvcols = csvrows[i].split(",");  
                    
                    //Looping through each cell in a csv row    
                    let Age = csvcols[0];
                    let Gender = csvcols[1];
                    let Race = csvcols[2];
                    let Immigrant = csvcols[3];
                    let Education = csvcols[4];
                    let RelStatus = csvcols[5];
                    let Employed = csvcols[6];
                    let Work = csvcols[7];
                    let MilService = csvcols[8];
                    let Arrested = csvcols[9];
                    let ParentDivorce = csvcols[10];
                    let SES = csvcols[11];
                    let MentalIllness = csvcols[12];
                    let MentalIllnessHistory = csvcols[13];
                    let Autism = csvcols[14];
                    let HealthIssues = csvcols[15];

                    // Add row to database
                    // Get classification and probability
                    risk_url = 'http://127.0.0.1:5000/api/v1.0/blackbox/' 
                        + Age + '/' 
                        + Gender + '/'
                        + Race + '/'
                        + Immigrant + '/'
                        + Education.replaceAll("/", "+") + '/'
                        + RelStatus.replaceAll("/", "+") + '/'
                        + Employed + '/' 
                        + Work + '/' 
                        + MilService + '/' 
                        + Arrested + '/' 
                        + ParentDivorce + '/' 
                        + SES + '/' 
                        + MentalIllness + '/'
                        + MentalIllnessHistory + '/'
                        + Autism + '/'
                        + HealthIssues;

                    // Get probability from API
                    d3.json(risk_url).then(updateCount);
            }  
        }  
      
        reader.readAsText($("#csvfile")[0].files[0]);  
     
        } else {  
            alert("Sorry! Your browser does not support HTML5!");  
        }  
    
    } else {  
        alert("Please upload a valid CSV file!");  
    }  
}

// Show the number of entries when the page loads
updateCount();