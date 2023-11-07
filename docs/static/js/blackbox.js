// Global variables
let n_rows = 0

// Clear table
function clearTable() {
    let table = $("#csvtable > tbody");
    table.empty();
    n_rows = 0;
}

// Source: https://www.c-sharpcorner.com/blogs/reading-a-csv-file-using-html5-jquery
function loadData() {  
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
                if (csvrows[i] != "") {  
                    var row = "<tr>";  
                    var csvcols = csvrows[i].split(",");  
                    
                    //Looping through each cell in a csv row    
                    for (var j = 0; j < csvcols.length; j++) {  
                        var cols = "<td>" + csvcols[j] + "</td>";  
                        row += cols;

                        // Add an extra column at the end for the probability
                        if (j == csvcols.length-1) {
                            row += "<td></td>"
                        }
                    }  
         
                    row += "</tr>";  
                    table.append(row);  
                }  
            }  
            $('#csvtable').show();  
        }  
      
        reader.readAsText($("#csvfile")[0].files[0]);  
     
        } else {  
            alert("Sorry! Your browser does not support HTML5!");  
        }  
    
    } else {  
        alert("Please upload a valid CSV file!");  
    }  
}

function displayRisk(data) {
    // Select current row
    let row = d3.select(`#csvtable>tbody>tr:nth-child(${data.ID})`);
    row.select('td:nth-child(17)').text(data.Classification);
    row.select('td:nth-child(18)').text(data.Probability);
}

function loopThroughTable() {
    console.log('Click')

    for (let i = 1; i<n_rows; i++) {
        console.log(`Row: ${i}`);

        // Select current row
        let row = d3.select(`#csvtable>tbody>tr:nth-child(${i})`);

        // Retrieve all elements
        let Age = row.select('td').text();
        let Gender = row.select('td:nth-child(2)').text();
        let Race = row.select('td:nth-child(3)').text();
        let Immigrant = row.select('td:nth-child(4)').text();
        let Education = row.select('td:nth-child(5)').text();
        let RelStatus = row.select('td:nth-child(6)').text();
        let Employed = row.select('td:nth-child(7)').text();
        let Work = row.select('td:nth-child(8)').text();
        let MilService = row.select('td:nth-child(9)').text();
        let Arrested = row.select('td:nth-child(10)').text();
        let ParentDivorce = row.select('td:nth-child(11)').text();
        let SES = row.select('td:nth-child(12)').text();
        let MentalIllness = row.select('td:nth-child(13)').text();
        let MentalIllnessHistory = row.select('td:nth-child(14)').text();
        let Autism = row.select('td:nth-child(15)').text();
        let HealthIssues = row.select('td:nth-child(16)').text();

        // Get classification and probability
        risk_url = 'http://127.0.0.1:5000/api/v1.0/blackbox/' + i + '/' + Age + '/' 
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
        d3.json(risk_url).then(displayRisk);
    }

    alert("Analysis completed.")
}
