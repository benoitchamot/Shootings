def replace_code_by_value(df, field, codes_dict):
    # Replace code by explicit value for each code in field
    for key in list(codes_dict.keys()):
        df.loc[df[field]==key,field] = codes_dict[key]
        

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
codes_shooter_background_birth = {
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
    0: 'Not working',
    1: 'Working'
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