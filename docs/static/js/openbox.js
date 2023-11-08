let state = 'AK';
let age_bracket = 'Under 10 years old';
let mental_illness = 0;
let employment = 1;
let arrest = 0;
let autism = 0;

let risk = 1;

function displayRisk(data) {
    let total_risk = data.Risk[0]*data.Risk[1]*data.Risk[2]*data.Risk[3]*data.Risk[4]
    displayGauge(total_risk);

    if (total_risk < 10) {
        d3.select('#risk_category').text("Low");
        d3.select('#risk_value').html("The prospect does not present a siginifcant risk.");
    }
    else if (total_risk < 100) {
        d3.select('#risk_category').text("Medium");
        d3.select('#risk_value').html("Proceed with care. Perform background checks.");
    }
    else if (total_risk < 1000) {
        d3.select('#risk_category').text("High")
        d3.select('#risk_value').html("Potential danger. Perform detailed background checks.");
    }
    else {
        d3.select('#risk_category').text("Very High");
        d3.select('#risk_value').html("Do not proceed with the transaction.");
    }

    if (age_bracket == 'Under 10 years old' || age_bracket == '10 to 14 years' || age_bracket == '15 to 17 years') {
        d3.select('#risk_category').text("STOP: Not allowed")
        d3.select('#risk_value').text("Prospect is too young to have a gun.");
    }

    // Format number
    let formatRisk = d3.format(".1f");

    // Update text for mental illness
    if (data.Risk[1] && data.Risk[1] != 1) {
        d3.select('#p_mental').html("The prospect suffers from some <strong>mental illness</strong>. The associated contribution to the overall Risk Factor is " + formatRisk(data.Risk[1]) + ".");
    } else if (data.Risk[1] && data.Risk[1] == 1) {
        d3.select('#p_mental').html("The prospect does not appear to suffer from any mental illness. There is no contribution to the Risk Factor.");
    }

    // Update text for employment status
    if (data.Risk[2] && data.Risk[2] != 1) {
        d3.select('#p_employ').html("The prospect is <strong>unemployed</strong>. The associated contribution to the overall Risk Factor is " + formatRisk(data.Risk[2]) + ".");
    } else if (data.Risk[2] && data.Risk[2] == 1) {
        d3.select('#p_employ').html("The prospect appears to be employed. There is no contribution to the Risk Factor.");
    }

    // Update text for previous arrest
    if (data.Risk[3] && data.Risk[3] != 1) {
        d3.select('#p_arrest').html("The prospect has been <strong>arrested before</strong>. The associated contribution to the overall Risk Factor is " + formatRisk(data.Risk[3]) + ".");
    } else if (data.Risk[3] && data.Risk[3] == 1) {
        d3.select('#p_arrest').html("The prospect does not appear to have ever been arrested. There is no contribution to the Risk Factor.");
    }

    // Update text for autism
    if (data.Risk[4] && data.Risk[4] != 1) {
        d3.select('#p_autism').html("The prospect is on the <strong>autism spectrum</strong>. The associated contribution to the overall Risk Factor is " + formatRisk(data.Risk[4]) + ".");
    } else if (data.Risk[4] && data.Risk[4] == 1) {
        d3.select('#p_autism').html("The prospect is not on the autism spectrum. There is no contribution to the Risk Factor.");
    }
    
}

function calculate_risk() {
    risk_url = 'http://127.0.0.1:5000/api/v1.0/openbox/' + state + '/' + age_bracket + '/' + mental_illness + '/' + employment + '/' + arrest + '/' + autism;
    d3.json(risk_url).then(displayRisk);
}

function get_state(value) {
    state = value;
    calculate_risk();
}

function get_age(value) {
    age_bracket = value;
    calculate_risk();
}

function check_mental(value) {
    mental_illness = value;
    calculate_risk();
}

function check_employment(value) {
    employment = value;
    calculate_risk();
}

function check_arrested(value) {
    arrest = value;
    calculate_risk();
    console.log(value);
}

function check_autism(value) {
    autism = value;
    calculate_risk();
}

calculate_risk();