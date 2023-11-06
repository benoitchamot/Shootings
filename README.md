# Shootings

## Limitations and future work
- Consolidate data for a single year or period. The current models are built with data from different years between 2018 and 2021. Data are assumed to be constant or at least comparable and interchangeable from one year to another and data from different years are used to complete the datasets when required. For instance, arrests data for 2018 from the FBI where used but the data for Iowa were incomplete and were simply replaced by 2019 data for that state. No verification has been performed to make sure that such a swap in data was valid and justified.
- Add more conditions to compare with the general population, such as: alcohol and drug use, head injuries, prejudices, firearms preficiency and interest, etc.
- Add data from more gun-related crimes. The current models only consider mass shootings. While this is the most dramatic type of gun violence, they are still rare events compared to gang-related violence, domestic violence and other crimes where firearms are involved. Adding more data could allow to refine the shooter profiles and increase the accuracy of the models.


## Data Sources
- **Shooter information**: Peterson, J., & Densley, J. (2023). The Violence Project database of mass shootings in the United States (Version 7). https://www.theviolenceproject.org
- **Mental Illness Information**: States with the highest levels of mental health illness - NiceRx. https://worldpopulationreview.com/state-rankings/mental-health-statistics-by-state
- **Unemployment Data**: Unemployment Rates for States - U.S. Bureau of Labor Statistics (2023). https://worldpopulationreview.com/state-rankings/unemployment-rate-by-state
- **Arrests by State**: Federal Bureau of Investigation (2018). https://ucr.fbi.gov/crime-in-the-u.s/2018/crime-in-the-u.s.-2018/topic-pages/tables/table-69 (Data for Iowa based on 2019 figures due to lack of information in 2018)
- **Autism prevalence**: National Library of Medicine, J Autism Dev Disord. 2020 Dec; 50(12): 4258–4266. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9128411/table/T2/
- **Other census datan**: U.S. Census Bureau (2018-2021). Accessed through `census` Python module API
