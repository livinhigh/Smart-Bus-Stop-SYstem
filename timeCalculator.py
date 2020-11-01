
# importing required libraries
import requests, json

def getTime(a,b):
# enter your api key here
    api_key ="AIzaSyBPBiXDpPPLX_w2FYUx-w-A_6rshINox3c"

    # Take source as input
    source = a

    # Take destination as input
    dest = b

    # url variable store url
    url ='https://maps.googleapis.com/maps/api/distancematrix/json?'

    # Get method of requests module
    # return response object
    print(url + 'origins=' + source +
                       '&destinations=' + dest +
                       '&key=' + api_key)
    r = requests.get(url + 'origins=' + source +
                       '&destinations=' + dest +
                       '&key=' + api_key)

    # json method of response object
    # return json format result
    x = r.json()

    # by default driving mode considered

    # print the value of x
    return x['rows'][0]['elements'][0]['duration']['text']
