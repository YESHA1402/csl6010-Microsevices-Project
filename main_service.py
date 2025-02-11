from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

user_service_url = "http://192.168.126.130"
order_service_url = "http://192.168.126.131"


@app.route("/")
def home():
	return jsonify({"message": "Main API Gateway is running..."}), 200

@app.route("/user", methods=['GET'])
def get_user():
	try:
		response = requests.get(f"{user_service_url}/user", timeout=5)
		return jsonify(response.json()), response.status_code
	except requests.excpetions.RequestException as e:
		return jsonify({"error": "User Service Not Available", "details": str(e)}), 500

@app.route("/orders", methods=['GET'])
def get_orders():
	try:
		response = requests.get(f"{order_service_url}/orders", timeout=5)
		return jsonify(response.json()), response.status_code
	except requests.exception.RequestException as e:
		return jsonify({"error": "Order Service Not Available", "details": str(e)}), 500


if __name__ == "__main__":
	app.run(host = "0.0.0.0", port=5000)
