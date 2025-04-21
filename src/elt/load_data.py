from src.etl.get_census_data import get_census_data

def run_full_pipeline():
    acs = get_census_data()
    # Join, clean, and save
    ...

if __name__ == "__main__":
    run_full_pipeline()
    
    
    
