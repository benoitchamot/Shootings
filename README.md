# Make America Safe... Again?

## Prerequisites
### API keys
To complete the ETL steps, the following APIs are used that need keys:
- Create a module named `config.py` in `/ETL`
- Add a variable called `api_census_key` and containing your US census API key in `config.py`
No prerequisites are needed to run the dashboard itself.

## How to build the project from scratch (optional)
The project contained in this repository is ready to run once the prerequesites are met.

However, if you would like to start with a blank sheet, the following steps can be followed

### Preparation
- Delete all CSV files in `/clean_data`
- Delete `blackbox_db.sqlite` and `openbox_db.sqlite` in `/Server`
- Delete `blackbox.model` in `/Server`

### Download the Violence Project Shooter Database
The Violence Project Shooter Database can be accessed under non-commercial license and may not be distributed without the authors' consent. It is therefore not included in this repository.

To run the project from sratch, the database must be added using the following steps:

- Obtain the Database Version 7 (Updated June 2023) in XLSX format from https://www.theviolenceproject.org/ 
- Convert the tab `Full Database` in the XLSX to a CSV file called `full_database.csv`
- Add `full_database.csv` to `/raw_data`

### ETL process (all notebooks are in `/ETL`)
1. Run `ETL_shooters_data_to_csv.ipynb`, make sure that `clean_shooters.csv` is created in `/Datasets/clean_data`
2. Run `ETL_autism_data_to_csv.ipynb`, make sure that `clean_autism.csv` is created in `/Datasets/clean_data`
3. Run `ETL_census_data_to_csv.ipynb`, make sure that `clean_male_population_age.csv` is created in `/Datasets/clean_data` and `population_stats.csv` in `/ETL`
4. Run `ETL_risks_to_openbox_db.ipynb`, make sure that `openbox_db.sqlite` is created in `/Server`
5. Run `ETL_shooters_data_to_db.ipynb`, make sure that `openbox_db.sqlite` is created in `/Server` and `model_blackbox_shooters.csv` in `/Model`
6. Run `Create_general_population_data.ipynb`, make sure that `model_blackbox_genpop.csv` is created in `/Model` (optionally, you can also create other CSV files in `/Examples`)

### Model training (all notebooks are in `/Model`)
1. Follow the ETL process (above) first and make sure all the necessary files are created as expected
2. Run `Model_training.ipynb`, make sure that `blackbox.model` and `blackbox.scaler` are created in `/Model`

## How to run the Web App

### Launch the Web App
Open `index.html` (in `/docs`) in any browser (Google Chrome is recommended.)

Note that the current version of the Web App only runs locally and is not hosted on the web.

### Start Flask Server
1. Navigate to `/Model`
2. Start Flask by using the command `python flask_app.py`
3. Check your console to make sure Flask is running
4. Navigate to the address indicated in the console

### Add, analyse and delete data

## File structure
### Directories
- `clean_data` contains all the CSV files extracted or created as part of the ETL process
- `docs` contains the HTML, JavaScript and CSS used to create the Web App
- `ETL` contains files to extract data from API or through web scraping and downloaded CSV files, transform the data, and load them into databases or clean CSV files
- `Examples` contains CSV files that can be used in the Web App for demonstration or test purposes
- `Model` contains the files used to design, train and test the Machine Learning models
- `Server` contains the Flask code, the saved (pickled) models, the Python modules used in the Flask app, and the SQLite databases

## Dataflow

## Analysis

### Research questions

### Bayesian approach (OpenBox)

### Machine Learning approach (BlackBox)

### Conclusions

### Limitations and future work
- Consolidate data for a single year or period. The current models are built with data from different years between 2018 and 2021. Data are assumed to be constant or at least comparable and interchangeable from one year to another and data from different years are used to complete the datasets when required. For instance, arrests data for 2018 from the FBI where used but the data for Iowa were incomplete and were simply replaced by 2019 data for that state. No verification has been performed to make sure that such a swap in data was valid and justified.
- Add more conditions to compare with the general population, such as: alcohol and drug use, head injuries, prejudices, firearms preficiency and interest, etc.
- Add data from more gun-related crimes. The current models only consider mass shootings. While this is the most dramatic type of gun violence, they are still rare events compared to gang-related violence, domestic violence and other crimes where firearms are involved. Adding more data could allow to refine the shooter profiles and increase the accuracy of the models.


### Data Sources
- **Shooter information**: Peterson, J., & Densley, J. (2023). The Violence Project database of mass shootings in the United States (Version 7). https://www.theviolenceproject.org
- **Mental Illness Information**: States with the highest levels of mental health illness - NiceRx. https://worldpopulationreview.com/state-rankings/mental-health-statistics-by-state
- **Unemployment Data**: Unemployment Rates for States - U.S. Bureau of Labor Statistics (2023). https://worldpopulationreview.com/state-rankings/unemployment-rate-by-state
- **Arrests by State**: Federal Bureau of Investigation (2018). https://ucr.fbi.gov/crime-in-the-u.s/2018/crime-in-the-u.s.-2018/topic-pages/tables/table-69 (Data for Iowa based on 2019 figures due to lack of information in 2018)
- **Autism prevalence**: National Library of Medicine, J Autism Dev Disord. 2020 Dec; 50(12): 4258–4266. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9128411/table/T2/
- **Other census datan**: U.S. Census Bureau (2018-2021). Accessed through `census` Python module API
