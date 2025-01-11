import googlemaps
import requests

apiKey="AIzaSyB8N3cgIEi8Ww2igo5I_uY9ikn9YocvNKk"

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

print(extract_coords(userLocation, apiKey))