let state = 'AK';
let age_bracket = 'Under 10 years old';
let mental_illness = 0;
let employment = 0;
let arrest = 0;
let autism = 0;

let risk = 1;

function displayRisk(data) {
    let total_risk = data.Risk[0]*data.Risk[1]*data.Risk[2]*data.Risk[3]*data.Risk[4]
    console.log(total_risk);

    if (age_bracket == 'Under 10 years old' || age_bracket == '10 to 14 years' || age_bracket == '15 to 17 years') {
        d3.select('#risk_category').text("Not allowed")
        d3.select('#risk_value').text("Prospect is too young to have a gun.");
    }
    else {
        d3.select('#risk_value').text(total_risk);
    }

    if (total_risk < 10) {
        d3.select('#risk_category').text("Risk: Low")
    }
    else if (total_risk < 100) {
        d3.select('#risk_category').text("Risk: Medium")
    }
    else if (total_risk < 1000) {
        d3.select('#risk_category').text("Risk: High")
    }
    else {
        d3.select('#risk_category').text("Risk: Very High")
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
}

function check_autism(value) {
    autism = value;
    calculate_risk();
}