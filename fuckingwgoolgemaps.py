#i cant actually test this code so it might be bs
import googlemaps
import requests
import pandas as pd

apiKey="AIzaSyB8N3cgIEi8Ww2igo5I_uY9ikn9YocvNKk"

map_client = googlemaps.Client(key = apiKey)
#this is gonna get replaced by smth got through the tinder system
types=['indian_restaurant','lebanese_restaurant']
#verify that keywords dont have to be one word
keywords=['indian food','shawarma']

#if i get an error in this section it could be because i enabled the geocoding api after i had already created the key
#also i removed the accents from that address cuase theyve caused problems before but that could make it invalid idk
userLocation='3200 Chem. de la Cote-Sainte-Catherine, Montreal, QC H3T 1C1'

def extract_coords(address,key):
    lat, lng = None, None
    api_key = key
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={address}&key={api_key}"
    # see how our endpoint includes our API key? Yes this is yet another reason to restrict the key
    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None, None
    try:
        '''
        This try block incase any of our inputs are invalid. This is done instead
        of actually writing out handlers for all kinds of responses.
        '''
        #lowkey i dont know what this is doing
        results = r.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
    except:
        pass
    return (lat,lng)

coords=extract_coords(userLocation,apiKey)
#this would be set by the user but try to keep low in demos to keep requests to a minimum
radius=100


results=[]

#code for types
for tag in types:
    response=map_client.places_nearby(location=coords,type=tag,rankby='distance',radius=radius)
    results.extend(response['result'])
    #in most example codes theyll tell you to then do a next pagr but likr is that necessary considering were doing multiple

#code for keywords in case we need it
#for tag in keywords:
    #parameters might be in the wrong order here
    #response=map_client.places_nearby(location=coords,keyword=tag,rankby='distance',radius=radius)
    #results.extend(response['result'])


#in theory at this point we have a list containing max 20 items for each type/keyword put in

#this functions as a way to confirm im getting results but i need a better way to display
print(len(results))

#im lowkey scared that theres a step missing 
df=pd.DataFrame(results)
