# geocoding

Hi, this is an api for geocoding.
(Using google maps api.)
## Endpoint(use with POST request)
https://geocoding07.herokuapp.com/getAddressDetails


## example usage:
send a post request with the api with the following parameters:
    
    {
    "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar,
    Bengaluru, Karnataka 560008",
    "output_format": "json"
    }
    
and it'll respond with it's coordinates(the output can be in json or xml format)    

# Try it on Postman
[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/17302941-11aae902-de47-4501-9ede-167773f46c4b?action=collection%2Ffork&collection-url=entityId%3D17302941-11aae902-de47-4501-9ede-167773f46c4b%26entityType%3Dcollection%26workspaceId%3D549bc406-a7d0-4e1e-beb7-3ec206ae1a8b)

    
    