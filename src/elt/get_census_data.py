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

def get_census_data(year: int = 2022, dataset = "acs/acs5", variables:list = None, for_clause = "county:*", in_clause = "state:*"):
    """
    Args:
        :param year: Year of the data, base is 2022 for testing
        :param dataset: dataset slug 
        :param variables: List of variables to pull from the census API 
        :param for_clause: base is counyt level data since this project is focused on county.
    Returns: 
        pd.DataFrame
    """
    if variables is None:
        variables = ["NAME", "B01003_001E", "B17001_002E"] #population, pop below poverty
        
    var_str = ",".join(variables) #creating variable list for the ceneus url that joins them with comma
    url = f"{CENSUS_API_BASE}/{year}/{dataset}?get={var_str}&for={for_clause}&in={in_clause}&key={API_KEY}" #creating URL using all variables thus far.
    
    logging.info(f"Requesting data for year {year} from Census API...")
    logging.debug(f"Request URL: {url}")

    start_time = time.time()
    response = requests.get(url)
    elapsed = time.time() - start_time

    try:
        response.raise_for_status()
        logging.info(f"✅ Success: Received data in {elapsed:.2f} seconds.")
    except requests.exceptions.HTTPError as err:
        logging.error(f"❌ HTTP Error: {err}")
        raise
    
    response = requests.get(url)
    response.raise_for_status() #kicks back an error if there is one.
    
    data = response.json() #saving data as json
    df = pd.DataFrame(data[1:], columns = data[0])
    logging.info(f"📊 Returned {len(df)} rows and {len(df.columns)} columns.")
    return df
    
df = get_census_data()
df.to_pickle("data/raw/acs_2022.pkl")