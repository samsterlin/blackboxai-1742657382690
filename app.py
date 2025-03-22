from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Serve static files
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/vehicle', methods=['POST'])
def verify_vehicle():
    try:
        vehicle_number = request.json.get('registrationNumber')
        # Mock response for demo
        return jsonify({
            "registrationNumber": vehicle_number,
            "ownerName": "Sample Owner",
            "registrationDate": "2020-01-01",
            "vehicleClass": "MCWG",
            "fuelType": "PETROL",
            "makerName": "HONDA",
            "modelName": "CITY",
            "status": "ACTIVE",
            "taxValidUpto": "2024-12-31",
            "insuranceValidUpto": "2024-06-30",
            "fcValidUpto": "2024-12-31",
            "pucValidUpto": "2024-03-31",
            "rcStatus": "ACTIVE"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/license', methods=['POST'])
def verify_license():
    try:
        license_number = request.json.get('licenseNumber')
        dob = request.json.get('dob')
        # Mock response for demo
        return jsonify({
            "dlNumber": license_number,
            "holderName": "Sample Name",
            "fatherName": "Sample Father Name",
            "issueDate": "2020-01-01",
            "validFrom": "2020-01-01",
            "validUpto": "2040-12-31",
            "vehicleClass": ["LMV", "MCWG"],
            "issuingAuthority": "RTO Chennai",
            "status": "ACTIVE",
            "bloodGroup": "O+",
            "permanentAddress": "123, Sample Street, Chennai - 600001",
            "badgeNumber": "TN12345",
            "lastTransactionAt": "2023-12-31"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)