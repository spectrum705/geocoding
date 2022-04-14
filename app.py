from flask import Flask, abort, request, json
from flask import jsonify
import requests
import os

#create flask app
API_KEY = os.environ['API_KEY']

app=Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message':'welcome to geolocation api'})
		
@app.route('/getAddressDetails', methods=['POST'])
def getAddressDetails():
    request_data = request.get_json()

  
    try:
        location = request_data["address"]
        output_type = request_data["output_format"]
        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={API_KEY}'
        mid = requests.get(url)
        res=mid.json()
        cord=res['results'][0]['geometry']['location']
        addrs=res['results'][0]['formatted_address']
        if output_type=="json":
            data={
                "coordinates":{
                "latitude":cord['lat'],
                "longitude":cord['lng'],},
                "address":addrs
            }
            return jsonify(data)
        elif output_type=="xml":
            return f""" <?xml version="1.0" encoding="UTF-8"?>
                    <root>
                    <address>{addrs}</address>
                    <coordinates>
                    <lat>{cord['lat']}</lat>
                    <lng>{cord['lng']}</lng>
                    </coordinates>
                    </root>""", 200
    except:
        return jsonify({'error':"something went wrong, please try again"}), 400

if __name__ == '__main__':
    app.run(debug=True)
    