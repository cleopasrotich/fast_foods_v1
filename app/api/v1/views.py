from flask import Flask, jsonify, abort, request, make_response

app = Flask(__name__)

orders = []


@app.route('/fast_foods/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify(
        {"orders": orders}
    )


@app.route('/fast_foods/api/v1/orders/<int:order_id>', methods=['GET'])
def get_task(order_id):
    required_order = []
    for order in orders:
        if order['id'] == order_id:
            required_order.append(order)
    if len(required_order) == 0:
        abort(404)

    return jsonify({'order': required_order[0]})


@app.route('/fast_foods/api/v1/orders', methods=['POST'])
def place_order():
    if not request.json:  # or  'summary' in request.json:
        abort(404)

    order = [
        {
            'id': int(request.json['id']),
            'name': request.json['name'],
            'location': request.json['location'],
            'summary': request.json['summary'],
            'quantity': request.json['quantity'],
            'total': str(int(request.json['quantity']) * 250),
            'accepted': True
        }
    ]

    orders.append(order[0])
    return jsonify({
        'order': order
    }), 201


@app.route('/fast_foods/api/v1/orders/<int:order_id>', methods=['PUT'])
def edit_order(order_id):
    required_order = []
    for order in orders:
        if order['id'] == order_id:
            required_order.append(order)
    required_order[0]['name'] = request.json['name']
    required_order[0]['location'] = request.json['location']
    required_order[0]['summary'] = request.json['summary']
    required_order[0]['quantity'] = request.json['quantity']
    return jsonify({'orders': required_order[0]})


@app.route('/fast_foods/api/v1/orders/<int:order_id>', methods=['DELETE'])
def remove_order(order_id):
    required_order = []
    for order in orders:
        if order['id'] == order_id:
            required_order.append(order)
    orders.remove(required_order[0])
    return jsonify({'orders': orders})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
