import time
from geopy.geocoders import Nominatim

geolocator = Nominatim( user_agent='geopiExercises' )

def get_longlat( x ):
    index, row = x
    time.sleep(1)
    response = geolocator.reverse( row['query'] )
    address = response.raw['address']

    try:
        place_id = response.raw['place_id'] if 'place_id' in response.raw else 'NA'        
        display_name = address['display_name'] if 'display_name' in address else 'NA'
        neighbourhood = address['neighbourhood'] if 'neighbourhood' in address else 'NA'
        
     

        return place_id, display_name, neighbourhood

    except:
        return None, None, None, None


   