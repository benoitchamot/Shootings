import pandas as pd

###### FUNCTION ##################################################################################
def replace_code_by_value(df, field, codes_dict):
    # Replace code by explicit value for each code in field
    for key in list(codes_dict.keys()):
        df.loc[df[field]==key,field] = codes_dict[key]

def get_distribution(df, field, codes):
# Return a DataFrame with counts and distribution (percent)
# In: DataFrame to analyse
# In: Field of DataFrame to analyse (string)
# In: Codes to replace numerical values by categorical values
# Out: DataFrame with: Value | Count | Percent
    if codes:
        replace_code_by_value(df, field, codes)
    stat_df = pd.DataFrame(df[field].value_counts())
    total_count = stat_df[field].sum()
    stat_df['Percent'] = 100*stat_df[field]/total_count
    return stat_df
        

###### CODES FOR SHOOTERS ########################################################################
###### BACKGROUND ######################################################
# Gender codes
codes_shooter_background_gender = {
     0: 'Male',
     1: 'Female',
     3: 'Non-Binary',
     4: 'Transgender'
}

# Race codes
codes_shooter_background_race = {
    -1: 'Unknown',
    0: 'White',
    1: 'Black',
    2: 'Latinx',
    3: 'Asian',
    4: 'Middle Eastern',
    5: 'Native American'     
}

# Immigrant codes
codes_shooter_background_immigrant = {
    -1: 'Unknown',
    0: 'No',
    1: 'Yes',    
}

# Sexual orientation codes
codes_shooter_background_sexorient = {
    -1: 'Unknown',
    0: 'Heterosexual',
    1: 'Not Heterosexual' 
}

# Religion codes
codes_shooter_background_religion = {
    -1: 'Unknown',
    0: 'None',
    1: 'Christian',  
    2: 'Muslim',  
    3: 'Buddhist',  
    4: 'Other',  
    5: 'Jewish'  
}

# Education codes
codes_shooter_background_education = {
    -1: 'Unknown',
    0: 'Less than high school',
    1: 'High school/GED',
    2: 'Some college/trade school',
    3: "Bachelor's degree",
    4: 'Graduate school/advanced degree',
}

# School performance code
codes_shooter_background_schoolperf = {
    -1: 'Unknown',
    0: 'Poor',
    1: 'Average',
    2: 'Good'
}

# Birth order code
codes_shooter_background_birth = {
    -1: 'Unknown',
    0: 'Only child',
    1: 'Oldest child',
    2: 'Middle child',
    3: 'Youngest child',
    4: 'Twin'
}

# Relationship status code
codes_shooter_background_relationship = {
    -1: 'Unknown',
    0: 'Single',
    1: 'Boyfriend/girlfriend',
    2: 'Married',
    3: 'Divorced/separated/widowed'
}

# Children code
codes_shooter_background_children = {
    0: 'No evidence',
    1: 'Yes',
}

# Employment status code
codes_shooter_background_employstatus = {
    -1: 'Unknown',
    0: 'No',
    1: 'Yes'
}

# Employment type code
codes_shooter_background_employtype = {
    -1: 'Unknown',
    0: 'Blue collar',
    1: 'White collar',
    2: 'In between'
}

# Military service code
codes_shooter_background_milservice = {
    -1: 'Unknown',
    0: 'No',
    1: 'Yes',
    2: 'Joined but did not make it through training'
}

# Military branch code
codes_shooter_background_milbranch = {
    -1: 'NA',
    0: 'Army',
    1: 'Navy',
    2: 'Air Force',
    3: 'Marines',
    4: 'Coast Guard',
    5: 'National Guard'
}

# Community involvement code
codes_shooter_background_community = {
    0: 'No evidence',
    1: 'Somewhat involved',
    2: 'Heavily involved',
    3: 'Recently withdrawn'

}

###### CRIME AND VIOLENCE ######################################################
# Known to Police or FBI
codes_shooter_crime_known = {
    0: 'No evidence',
    1: 'Yes'
}

# Criminal Record
codes_shooter_crime_record = {
    0: 'No evidence',
    1: 'Yes'   
}

# Part 1 Crimes
codes_shooter_crime_part1 = {
    0: 'No evidence',
    1: 'Homicide',
    2: 'Forcible rape',
    3: 'Robbery',
    4: 'Aggravated Assault',
    5: 'Burglary',
    6: 'Larceny-Theft',
    7: 'Motor Vehicle Theft',
    8: 'Arson',
}

# Part 2 Crimes
codes_shooter_crime_part2 = {
    0: 'No evidence',
    1: 'Simple assault',
    2: 'Fraud, forgery, embezzlement',
    3: 'Stolen property',
    4: 'Vandalism',
    5: 'Weapons offenses',
    6: 'Prostitution or other non-rape sex offenses',
    7: 'Drugs',
    8: 'DUI',
    9: 'Other'
}

# Highest level of criminal justice involvement
codes_shooter_crime_justice = {
    0: 'NA',
    1: 'Suspected',
    2: 'Arrested',
    3: 'Charged',
    4: 'Convicted'
}

# Animal Abuse
codes_shooter_crime_animal = {
    0: 'No evidence',
    1: 'Yes'    
}

# History of Physical Altercations
codes_shooter_crime_physical = {
    0: 'No evidence',
    1: 'Yes',
    2: 'Attacked inanimate objects during arguments '
}

# History of domestic abuse
codes_shooter_crime_abuse = {
    0: 'No evidence',
    1: 'Abused romantic partner',
    2: 'Abused other family member(s)'
}

# History of sexual offenses 
codes_shooter_crime_sexual = {
    0: 'No evidence',
    1: 'Yes',
}

# Gang association
codes_shooter_crime_gang = {
    0: 'No evidence',
    1: 'Yes',
}

# Terror group association
codes_shooter_crime_terror = {
    0: 'No evidence',
    1: 'Yes',
}

# Hate group association
codes_shooter_crime_hate = {
    0: 'No evidence',
    1: 'Hate group community association',
    2: 'Other radical group association',
    3: 'Inspired by a hate group but no direct connection',
    4: 'Website or chat room postings relating to hate or hate groups'
}

# Played violent video games
codes_shooter_crime_games = {
    0: 'No evidence',
    1: 'Yes',
    2: 'Played unspecified video games',
    3: 'NA (pre-1992)'
}

# Bullly
codes_shooter_crime_bully = {
    0: 'No evidence',
    1: 'Yes'
}

###### TRAUMA AND ADVERSE CHILDHOOD EXPERIENCES ##########################################
# Bullied
codes_shooter_trauma_bully = {
    0: 'No evidence',
    1: 'Yes'
}

# Raised by single parent
codes_shooter_trauma_singleparent = {
    0: 'No evidence',
    1: 'Yes'
}

# Parental separation or divorce
codes_shooter_trauma_divorce = {
    0: 'No evidence',
    1: 'Yes'
}

# Suicide of parent
codes_shooter_trauma_suicide = {
    0: 'No evidence',
    1: 'Yes'
}

# Death of parent
codes_shooter_trauma_death = {
    0: 'No evidence',
    1: 'Yes'
}

# Childhood trauma
codes_shooter_trauma_childtrauma = {
    0: 'No evidence',
    1: 'Yes'
}

# Physical Abuse
codes_shooter_trauma_physical = {
    0: 'No evidence',
    1: 'Yes'
}

# Sexual Abuse
codes_shooter_trauma_sexual = {
    0: 'No evidence',
    1: 'Yes'
}

# Emotional Abuse
codes_shooter_trauma_emotional = {
    0: 'No evidence',
    1: 'Yes'
}

# Neglect
codes_shooter_trauma_neglect = {
    0: 'No evidence',
    1: 'Yes'
}

# Childhood socioeconomic status
codes_shooter_trauma_ses = {
    -1: 'Unknown',
    0: 'Lower class',
    1: 'Middle class',
    2: 'Upper class'
}

# Mother was violently treated
codes_shooter_trauma_violence = {
    0: 'No evidence',
    1: 'Yes'
}

# Parent substance abuse
codes_shooter_trauma_substance = {
    0: 'No evidence',
    1: 'Yes'
}

# Parent criminal record
codes_shooter_trauma_criminal = {
    0: 'No evidence',
    1: 'Yes'
}

# Family member incarcerated
codes_shooter_trauma_prison = {
    0: 'No evidence',
    1: 'Yes'
}

# Adult trauma
codes_shooter_trauma_adulttrauma = {
    0: 'No evidence',
    1: 'Death of a parent causing significant distress',
    2: 'Death or loss of a child',
    3: 'Death of a family member causing significant distress',
    4: 'Trauma from war',
    5: 'Traumatic accident',
    6: 'Other trauma'
}

###### SIGNS OF A CRISIS #######################################################
# Recent stressor / triggering event
codes_shooter_crisis_trigger = {
    -1: 'Unknown',
    0: 'No evidence',
    1: 'Recent break-up',
    2: 'Employment stressor',
    3: 'Economic stressor',
    4: 'Family issue',
    5: 'Legal issue',
    6: 'Other'
}

# Signs of being in crisis
codes_shooter_crisis_signs = {
    0: 'No evidence',
    1: 'Yes'
}

# Timeframe of when signs of crisis began
codes_shooter_crisis_timeframe = {
    -1: 'Unknown',
    0: 'Days before shooting',
    1: 'Weeks before shooting',
    2: 'Months before shooting',
    3: 'Years before shooting'
}

# Inability to perform daily tasks
codes_shooter_crisis_inability = {
    0: 'No evidence',
    1: 'Yes'
}

# Notably depressed mood
codes_shooter_crisis_depressed = {
    0: 'No evidence',
    1: 'Yes'
}

# Unusually calm or happy
codes_shooter_crisis_calm = {
    0: 'No evidence',
    1: 'Yes'
}

# Rapid mood swings
codes_shooter_crisis_swings = {
    0: 'No evidence',
    1: 'Yes'
}

# Increased agitation
codes_shooter_crisis_agitation = {
    0: 'No evidence',
    1: 'Yes'
}

# Abusive behavior
codes_shooter_crisis_abusive = {
    0: 'No evidence',
    1: 'Yes'
}

# Isolation
codes_shooter_crisis_isolation = {
    0: 'No evidence',
    1: 'Yes'
}

# Losing touch with reality 
codes_shooter_crisis_reality = {
    0: 'No evidence',
    1: 'Yes'
}

# Paranoia
codes_shooter_crisis_paranoia = {
    0: 'No evidence',
    1: 'Yes'
}

###### HEALTH AND MENTAL HEALTH ###################################################
# Suicidality
codes_shooter_health_suicide = {
    0: 'No evidence',
    1: 'Yes, at any point before the shooting',
    2: 'Intended to die in shooting but had no previous suicidality'
}

# Hospitalization for psychiatric reasons
codes_shooter_health_hospital = {
    0: 'No evidence',
    1: 'Yes'
}

# Voluntary or involuntary hospitalization
codes_shooter_health_voluntarryhospital = {
    0: 'NA',
    1: 'Voluntary',
    2: 'Involuntary'
}

# Prior counseling
codes_shooter_health_counseling = {
    0: 'No evidence',
    1: 'Yes'
}

# Voluntary or mandatory counseling
codes_shooter_health_mandatorycounseling = {
    0: 'NA',
    1: 'Voluntary',
    2: 'Involuntary'
}

# Prescribed psychiatric medication
codes_shooter_health_medication = {
    0: 'No evidence',
    1: 'Yes'
}

# Treatment
codes_shooter_health_treatment = {
    0: 'No evidence',
    1: 'Yes'
}

# Mental illness
codes_shooter_health_illness = {
    '0': 'No evidence',
    '1': 'Mood disorder',
    '1, 2': 'Mood disorder',
    '2': 'Thought disorder',
    '3': 'Other psychiatric disorder',
    '4': 'Indication of psychiatric disorder but no diagnosis'
}

# FASD (Fetal Alcohol Spectrum Disorder)
codes_shooter_health_fasd = {
    0: 'No evidence',
    1: 'Yes'
}

# Known family history of mental health issues
codes_shooter_health_family = {
    0: 'No evidence',
    1: 'Parents had mental health issues',
    2: 'Other close relatives had mental health issues'
}

# Autism spectrum disorder
codes_shooter_health_autism = {
    0: 'No evidence',
    1: 'Diagnosed or extremely likely'
}

# Substance use and abuse
codes_shooter_health_substance = {
    0: 'No evidence',
    1: 'Problem with alcohol',
    2: 'Marijuana',
    3: 'Other drugs'
}

# Health issues
codes_shooter_health_issues = {
    0: 'No evidence',
    1: 'Yes'
}

# Head injury / Possible brain injury
codes_shooter_health_head = {
    0: 'No evidence',
    1: 'Yes'
}

###### OTHER ###################################################
# Known prejudices
codes_shooter_other_prejudices = {
    0: 'No evidence',
    1: 'Racism',
    2: 'Misogyny',
    3: 'Homophobia',
    4: 'Religious hatred'
}

# Notable or obsessive interest in firearms
codes_shooter_other_interest = {
    0: 'No evidence',
    1: 'Yes'
}

# Firearm proficiency
codes_shooter_other_proficiency = {
    -1: 'Unknown',
    0: 'No experience',
    1: 'Some experience',
    2: 'More experienced',
    3: 'Very experienced'
}


###### CODES FOR FIREARMS ########################################################################
# Classification codes
codes_firearm_classification = {
    0: 'Handgun',
    1: 'Shotgun',
    2: 'Rifle',
    3: 'Assault weapon'
}

# Caliber codes
codes_firearm_caliber = {
    0: 'Small',
    1: 'Medium',
    2: 'Large'
}

# "Used in shooting" codes
codes_firearm_used = {
    0: 'No evidence',
    1: 'Yes',
    2: 'Suicide only'
}

# Modified codes
codes_firearm_modified = {
    0: 'No evidence',
    1: 'Yes'
}

# "Large Capacity Magazine" codes
codes_firearm_large_mag = {
    0: 'No evidence',
    1: 'Yes'
}

# "Extended magazine" codes
codes_firearm_extended_mag = {
    0: 'No evidence',
    1: 'Yes'
}

# "When obtained" codes
codes_firearm_when = {
    0: '< 1 month prior',
    1: '> 1 month prior'
}

# "Legal purchase" codes
codes_firearm_legal = {
    0: 'Illegal',
    1: 'Federal Firearms Licensed dealer',
    2: 'Unregulated private sale',
    3: 'Legal but specific source unknown'
}

# "Illegal purchase" codes
codes_firearm_illegal = {
    0: 'Legal',
    1: 'System failure',
    2: 'Straw purchas',
    3: 'Lying and buying',
    4: 'Illegal street sale',
    5: 'Illegal but specific source unknown',
    6: 'Legal sale but illegal possession'
}

# "Assembled with legal parts" codes
codes_firearm_assembly = {
    0: 'No',
    1: 'Yes'
}

# "Gifted" codes
codes_firearm_gifted = {
    0: 'No',
    1: 'Yes'
}
				
# Theft codes
codes_firearm_theft = {
    0: 'No',
    1: 'Theft/borrowed from family or friend',
    2: 'Theft other',
    3: 'Taken at the scene'
}

# "Unknown" codes
codes_firearm_unknown = {
    0: 'No',
    1: 'Yes'
}

###### CODES FOR US STATES ########################################################################
codes_states = {
    'Alabama': 'AL',
    'Kentucky': 'KY',
    'Ohio': 'OH',
    'Alaska': 'AK',
    'Louisiana': 'LA',
    'Oklahoma': 'OK',
    'Arizona': 'AZ',
    'Maine': 'ME',
    'Oregon': 'OR',
    'Arkansas': 'AR',
    'Maryland': 'MD',
    'Pennsylvania': 'PA',
    'American Samoa': 'AS',
    'Massachusetts': 'MA',
    'Puerto Rico': 'PR',
    'California': 'CA',
    'Michigan': 'MI',
    'Rhode Island': 'RI',
    'Colorado': 'CO',
    'Minnesota': 'MN',
    'South Carolina': 'SC',
    'Connecticut': 'CT',
    'Mississippi': 'MS',
    'South Dakota': 'SD',
    'Delaware': 'DE',
    'Missouri': 'MO',
    'Tennessee': 'TN',
    'District of Columbia': 'DC',
    'Montana': 'MT',
    'Texas': 'TX',
    'Florida': 'FL',
    'Nebraska': 'NE',
    'Trust Territories': 'TT',
    'Georgia': 'GA',
    'Nevada': 'NV',
    'Utah': 'UT',
    'Guam': 'GU',
    'New Hampshire': 'NH',
    'Vermont': 'VT',
    'Hawaii': 'HI',
    'New Jersey': 'NJ',
    'Virginia': 'VA',
    'Idaho': 'ID',
    'New Mexico': 'NM',
    'Virgin Islands': 'VI',
    'Illinois': 'IL',
    'New York': 'NY',
    'Washington': 'WA',
    'Indiana': 'IN',
    'North Carolina': 'NC',
    'West Virginia': 'WV',
    'Iowa': 'IA',
    'North Dakota': 'ND',
    'Wisconsin': 'WI',
    'Kansas': 'KS',
    'Northern Mariana Islands': 'MP',
    'Wyoming': 'WY'
}