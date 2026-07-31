import requests
import json
import logging
import pandas as pd
# configure logging format and level
logging.basicConfig(level=logging.INFO,
                    format= "%(asctime)s  - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
filepath = 'credentials.json'
def load_credentials(filepath):
    try:
        with open(filepath,mode= 'r') as file:
            return json.load(file)
    except Exception as E:
        logger.error("file does not exist:",{filepath}, E) 
def gettingapi(api):
    try:
        user = api['clientId']
        password = api['clientSecret']
        return user, password
    except Exception as E:
        logging.error("ERROR: ",E)

# fetching data from the server using api
def fetch_data_api(user,password):
    url = 'https://opensky-network.org/api/states/all'
    var = {
        'lamin' :  20.00,  # Widen North/South boundary
        'lamax' :  40.00,
        'lomin' :  60.00,  # Widen East/West boundary
        'lomax' :  85.00
    }
    logging.info('Initiating secure API request...')
    try:
         # Pass credentials safely using HTTP Basic Auth
        response = requests.get(url,params=var , auth=(user,password),timeout=10)
        # getting response into json and show 
        logging.info(response.json())
        # checking response form the server if it is 200 means succesfull
        response.raise_for_status()

        logging.info("succesfully! Extract data")
        return response.json()
    except Exception as E:
        logging.error('ERROR: ', {E})

def load_pandas(data):
    try:
        if not data or 'states' not in data or data['states'] is None:
            logging.warning("No live aircraft tracked within these coordinates right now.")
        return pd.DataFrame()
    except Exception as E:
        logging.info("ERROR: ",{E})

def clean_data(df):
    try:
        return df.head()
    except Exception as E:
        logging.error('ERROR: ',E)
api = load_credentials(filepath)
user_password = gettingapi(api)

json_data = logging.info(user_password)
data = fetch_data_api(*user_password)
df = load_pandas(data)

df_clean = clean_data(df)
logging.info(df_clean)
