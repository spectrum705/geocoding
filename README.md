# geocoding

Hi, this is an api for geocoding.
(Using google maps api.)
## Endpoint
/getAddressDetails
    
## example usage:
send a post request with the api with the following parameters:
    
    {
    "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar,
    Bengaluru, Karnataka 560008",
    "output_format": "json"
    }
    
and it'll respond with it's coordinates(the output can be in json or xml format)    
    
    