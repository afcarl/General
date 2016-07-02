

import argparse
import json
import pprint
import sys
import urllib
import urllib2
import pandas as pd
import numpy as np
import oauth2
import csv

df = pd.read_csv('cleandata.csv')
names = []
loc = []
# global API_HOST #= ""
# global DEFAULT_TERM #= ""
# global DEFAULT_LOCATION #= ""
# global SEARCH_LIMIT# = ""
# global SEARCH_PATH #= ""
# global BUSINESS_PATH #= ""

datelist = []
   

# def some(i):
#     API_HOST = 'api.yelp.com'
#     DEFAULT_TERM = names[i]
#     print DEFAULT_TERM,loc[i]
#     DEFAULT_LOCATION = loc[i]
#     SEARCH_LIMIT = 1
#     SEARCH_PATH = '/v2/search/'
#     BUSINESS_PATH = '/v2/business/'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = "cfcCUGuefQQwKTGNjoE0Lg"
CONSUMER_SECRET = "kq-fIb_37FfZJtjdGMXlhh6L3Gs"
TOKEN = "h6tOB2r_UQbQVfriEZY1NTiz_1_VTBUp"
TOKEN_SECRET = "oBPBMNmV65f2p3O3tx0DIPZIxcM"


def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = 'https://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request(
        method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(
        oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    print u'Querying {0} ...'.format(url)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response


def search(term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)


def get_business(business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path)


def query_api(term, location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(term, location)

    businesses = response.get('businesses')

    if not businesses:
        print u'No businesses for {0} in {1} found.'.format(term, location)
        return

    business_id = businesses[0]['id']

    print u'{0} businesses found, querying business info ' \
        'for the top result "{1}" ...'.format(
            len(businesses), business_id)
    response = get_business(business_id)
    return response
    print u'Result for business "{0}" found:'.format(business_id)
    pprint.pprint(response, indent=2)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    try:
        return query_api(input_values.term, input_values.location)
    except urllib2.HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0}. Abort program.'.format(error.code))
        pass        

rating = []
names = []
i = 0
loc = []
if __name__ == '__main__':
    for i in range(len(df)):
        names.append(df['DBA'][i])
        loc.append(df['STREET_ADDRESS'][i])
    # f = open("geoccleandata.csv" , "rt")
    # try:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print row
    #         names.append(str(row[0]))
    #         datelist.append(str(row[9]).split('York')[0]+str('York,NY'))

    # finally:

    #     f.close()



    some1 = []
    rating = []
    k = 0
    for i in range(262, 26000):
        
        API_HOST = 'api.yelp.com'
        DEFAULT_TERM = names[i]
        print DEFAULT_TERM,loc[i]
        DEFAULT_LOCATION = loc[i]
        SEARCH_LIMIT = 1
        SEARCH_PATH = '/v2/search/'
        BUSINESS_PATH = '/v2/business/'
        
        try: 
            qwerty = (main())
            print qwerty['rating']
            rating.append(qwerty['rating'])
        except:
            rating.append(0)
            pass    
        #rating.append(some1[i]['rating'])
        with open('q.csv', 'a') as csvfile:
            fieldnames = ['rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'rating':rating[k]})
            k = k+1
