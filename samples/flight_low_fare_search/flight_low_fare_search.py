from amadeus import Client, ResponseError

amadeus = Client()

print('Flight Low-Fare Search')
try:
    '''
    Find best flight offers from Madrid to New York
    '''
    response = amadeus.shopping.flight_offers.get(origin='MAD', destination='NYC', departureDate='2020-06-01')
    print(response.data)
except ResponseError as error:
    print(error)