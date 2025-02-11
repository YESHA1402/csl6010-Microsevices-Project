from flask import Flask, jsonify

app = Flask(__name__)

orders = [
	{"id": 1, "user_id": 1, "product": "Laptop", "status": "Shipped"},
	{"id": 2, "user_id": 2, "product": "Phone", "status": "Processing"}
]

@app.route('/orders', methods = ['GET'])
def get_orders():
	return jsonify(orders)

@app.route('/orders/<int:user_id>', methods = ['GET'])
def get_user_order(user_id):
	user_orders = [order for order in orders if order["user_id"] == user_id]
	return jsonify(user_orders) if user_orders else jsonify({"error": "No Order Found"}), 404

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5002)
