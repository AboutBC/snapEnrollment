#File to read in census data.

import logging
import time
import requests
import pandas as pd

CENSUS_API_BASE = "https://api.census.gov/data"
API_KEY = "0fe3adf3b896d3028a9eb63925e6b21506038b74"

logging.basicConfig(
    level=logging.INFO,  # Use DEBUG for more detail
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

def get_census_data(years = [2021,2022], dataset = "acs/acs5", variables:list = None, for_clause = "county:*", in_clause = "state:*"):
    """
    Args:
        :param year: Year of the data, base is 2022 for testing
        :param dataset: dataset slug 
        :param variables: List of variables to pull from the census API 
        :param for_clause: base is counyt level data since this project is focused on county.
    Returns: 
        pd.DataFrame
    """
    #Creating the variable string for the URL
    if variables is None:
        variables = ["NAME", "B01003_001E", "B17001_002E"] #population, pop below poverty
    # creating variable list for the ceneus url that joins them with comma
    var_str = ",".join(variables)
    
    #Go through each year in years list and return a single stacked DataFrame
    i_loop = 0
    all_data = []
    session = requests.Session()
    for year in years:
        url = f"{CENSUS_API_BASE}/{year}/{dataset}?get={var_str}&for={for_clause}&in={in_clause}&key={API_KEY}" #creating URL using all variables thus far.
        logging.info(f"Requesting data for year {year} from Census API...")
        logging.debug(f"Request URL: {url}")
        start_time = time.time()
        response = session.get(url)
        elapsed = time.time() - start_time
        try:
            response.raise_for_status()
            logging.info(f"✅ Success: Received data in {elapsed:.2f} seconds.")
        except requests.exceptions.HTTPError as err:
            logging.error(f"❌ HTTP Error: {err}")
            raise
        
        json_data = response.json() #saving data as json
        df = pd.DataFrame(json_data[1:], columns=json_data[0])
        df["year"] = year
        logging.info(f"📊 Returned {len(df)} rows and {len(df.columns)} columns.")
        all_data.append(df)
    return pd.concat(all_data, ignore_index=True)
    
    if __name__ == "__main__":
        get_census_data()