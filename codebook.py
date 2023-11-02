def replace_code_by_value(df, field, codes_dict):
    # Replace code by explicit value for each code in field
    for key in list(codes_dict.keys()):
        df.loc[df[field]==key,field] = codes_dict[key]
        

###### CODES FOR FIREARMS ######
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