from src.etl.get_census_data import get_census_data

def run_full_pipeline():
    #Define years, variables to fetch from each API
    years = list(range(2012, 2023))
    acs_variables = [
        "GEO_ID",  # FIPS code (state + county)
        "NAME",  # County Name
        "STATE_NAME",  # State Name
        "B01003_001E",  # Total population
        "B01001_002E",  # Total male population
        "B01001_026E",  # Total female population
        "B17001_002E",  # Total households below poverty level
        "B17001_003E",  # Households with income below poverty level
        "B17001_004E",  # Households with income 100-149% of poverty level
        "B17001_005E",  # Households with income 150-199% of poverty level
        "B17001_006E",  # Households with income 200-299% of poverty level
        "B17001_007E",  # Households with income above 300% of poverty level
        "B15003_022E",  # Adults with bachelor's degree or higher
        "B23025_005E",  # Labor force participation rate (total population)
        "B23025_006E",  # Employed population
        "B23025_007E",  # Unemployed population
        "B06012_002E",  # Median household income
        "B07001_001E",  # Total population in households
        "B19001_001E",  # Total households by income
        "B19001_002E",  # Households with income less than $10,000
        "B19001_003E",  # Households with income between $10,000 and $14,999
        "B19001_004E",  # Households with income between $15,000 and $24,999
        "B19001_005E",  # Households with income between $25,000 and $34,999
        "B19001_006E",  # Households with income between $35,000 and $49,999
        "B19001_007E",  # Households with income between $50,000 and $74,999
        "B19001_008E",  # Households with income between $75,000 and $99,999
        "B19001_009E",  # Households with income between $100,000 and $149,999
        "B19001_010E",  # Households with income between $150,000 and $199,999
        "B19001_011E",  # Households with income $200,000 or more
        "B09010_001E",  # Household composition (children under 18)
        "B06010_003E",  # Families with children
        "B06010_004E",  # Families with children under 18 with income below poverty
        "B09002_002E",  # Total household with children under 6 years old
        "B09002_003E",  # Households with children under 6 years old with income below poverty
        "B17006_001E",  # Total individuals in poverty by age group
        "B17006_002E",  # Individuals in poverty under 18 years old
        "B17006_003E",  # Individuals in poverty 18 to 64 years old
        "B17006_004E",  # Individuals in poverty 65 years and over
        "B03002_003E",  # Hispanic or Latino population
        "B02001_003E",  # Black or African American population
        "B02001_004E",  # American Indian or Alaska Native population
        "B02001_005E",  # Asian population
        "B02001_006E",  # Native Hawaiian or Other Pacific Islander population
        "B02001_007E",  # Some other race alone
        "B02001_008E",  # Two or more races
        "B25070_001E",  # Median home value
        "B25064_001E",  # Total housing units (occupied, owner-occupied, renter-occupied)
        "B25003_003E",  # Total owner-occupied housing units
        "B25003_004E",  # Total renter-occupied housing units
    ]
    acs_variables_dict = {
        "GEO_ID": "fips_code",  # Full FIPS code (state + county)
        "NAME": "county_name",  # County Name
        "STATE_NAME": "state_name",  # State Name
        "B01003_001E": "total_population",  # Total population
        "B01001_002E": "total_male_population",  # Total male population
        "B01001_026E": "total_female_population",  # Total female population
        "B17001_002E": "households_below_poverty",  # Total households below poverty level
        "B17001_003E": "households_income_below_poverty",  # Households with income below poverty level
        "B17001_004E": "households_income_100_149_poverty",  # Households with income 100-149% of poverty level
        "B17001_005E": "households_income_150_199_poverty",  # Households with income 150-199% of poverty level
        "B17001_006E": "households_income_200_299_poverty",  # Households with income 200-299% of poverty level
        "B17001_007E": "households_income_above_300_poverty",  # Households with income above 300% of poverty level
        "B15003_022E": "adults_with_bachelor_degree_or_higher",  # Adults with bachelor's degree or higher
        "B23025_005E": "labor_force_participation_rate",  # Labor force participation rate (total population)
        "B23025_006E": "employed_population",  # Employed population
        "B23025_007E": "unemployed_population",  # Unemployed population
        "B06012_002E": "median_household_income",  # Median household income
        "B07001_001E": "total_population_in_households",  # Total population in households
        "B19001_001E": "total_households_by_income",  # Total households by income
        "B19001_002E": "households_with_income_less_than_10000",  # Households with income less than $10,000
        "B19001_003E": "households_with_income_10000_to_14999",  # Households with income between $10,000 and $14,999
        "B19001_004E": "households_with_income_15000_to_24999",  # Households with income between $15,000 and $24,999
        "B19001_005E": "households_with_income_25000_to_34999",  # Households with income between $25,000 and $34,999
        "B19001_006E": "households_with_income_35000_to_49999",  # Households with income between $35,000 and $49,999
        "B19001_007E": "households_with_income_50000_to_74999",  # Households with income between $50,000 and $74,999
        "B19001_008E": "households_with_income_75000_to_99999",  # Households with income between $75,000 and $99,999
        "B19001_009E": "households_with_income_100000_to_149999",
        # Households with income between $100,000 and $149,999
        "B19001_010E": "households_with_income_150000_to_199999",
        # Households with income between $150,000 and $199,999
        "B19001_011E": "households_with_income_above_200000",  # Households with income $200,000 or more
        "B09010_001E": "household_composition_with_children",  # Household composition (children under 18)
        "B06010_003E": "families_with_children",  # Families with children
        "B06010_004E": "families_with_children_under_18_below_poverty",
        # Families with children under 18 with income below poverty
        "B09002_002E": "households_with_children_under_6_years",  # Total household with children under 6 years old
        "B09002_003E": "households_with_children_under_6_years_below_poverty",
        # Households with children under 6 years old with income below poverty
        "B17006_001E": "individuals_in_poverty_by_age",  # Total individuals in poverty by age group
        "B17006_002E": "individuals_in_poverty_under_18",  # Individuals in poverty under 18 years old
        "B17006_003E": "individuals_in_poverty_18_to_64",  # Individuals in poverty 18 to 64 years old
        "B17006_004E": "individuals_in_poverty_65_and_over",  # Individuals in poverty 65 years and over
        "B03002_003E": "hispanic_or_latino_population",  # Hispanic or Latino population
        "B02001_003E": "black_or_african_american_population",  # Black or African American population
        "B02001_004E": "american_indian_or_alaska_native_population",  # American Indian or Alaska Native population
        "B02001_005E": "asian_population",  # Asian population
        "B02001_006E": "native_hawaiian_or_pacific_islander_population",
        # Native Hawaiian or Other Pacific Islander population
        "B02001_007E": "some_other_race_population",  # Some other race alone
        "B02001_008E": "two_or_more_races_population",  # Two or more races
        "B25070_001E": "median_home_value",  # Median home value
        "B25064_001E": "total_housing_units",  # Total housing units (occupied, owner-occupied, renter-occupied)
        "B25003_003E": "owner_occupied_housing_units",  # Total owner-occupied housing units
        "B25003_004E": "renter_occupied_housing_units",  # Total renter-occupied housing units
    }

    #Load
    acs = get_census_data(years = years, variables = acs_variables)
    # Join, clean, and save
    
    
    #Save
    acs.to_pickle("data/processed/acs_2012_2022.pkl")
    ...

if __name__ == "__main__":
    run_full_pipeline()
    
    
    
