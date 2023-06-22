import logging
import os
from datetime import datetime

# this is the how to log file in a simple and good manned
LOG_FILE = f"{datetime.now().strftime('%m %d %Y %H %M %S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(log_path, exist_ok = True)


LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)




'''
... for testing of logger 

if __name__ == "__main__":
    logging.info("logging started ")
    
    
    '''