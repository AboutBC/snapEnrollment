#Creating a log file with it used in pipeline as default. 

import logging
import os
import sys
from logging.handlers import RotatingFileHandler




def setup_logger(name = "data_pipeline", log_file = "logs/data_pipeline.log", level = logging.INFO):
    #Create log folder if not there.
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    #logger object.
    logger = logging.getLogger(name) #initialize
    logger.setLevel(level) 
    
    #prevent logs from duplicating
    if not logger.handlers:
        #set File Handler
        fh = RotatingFileHandler(log_file, maxBytes=5_000_000, backupCount=3)
        fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(logging.StreamHandler(sys.stdout))
        
        #set Stream Handler (terminal).
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
        
        logger.addHandler(fh)
        logger.addHandler(ch)
        
    return logger