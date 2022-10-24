# https://upcitemdb.com/api/explorer#!/lookup/get_trial_lookup
# UCP:0012993441012

import requests

base = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters ={'upc':'012993441012'}
response = requests.get(base,params=parameters)

print(response.url)