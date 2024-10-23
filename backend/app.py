from flask import Flask, request, jsonify
import ast_builder  # Ensure these modules exist and are correct
import rule_composer
import rule_evaluator

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.get_json()
    rule_string = data['rule_string']
    try:
        ast = ast_builder.create_rule(rule_string)
        return jsonify(ast.to_dict()), 200  # Use to_dict() here
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.get_json()
    if 'rules' not in data:
        return jsonify({'error': "Missing 'rules' in request data"}), 400
    rules = data['rules']
    try:
        combined_ast = rule_composer.combine_rules(rules)
        return jsonify(combined_ast.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400



@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.get_json()
    print(data)  # Add this line to log incoming data
    try:
        rule_ast = data['rule_ast']  # This line raises KeyError if 'rule_ast' is not in data
        attributes = data['attributes']
        result = rule_evaluator.evaluate_rule(rule_ast, attributes)
        return jsonify({'result': result}), 200
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400  # Handle missing keys gracefully
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    print("Starting Flask application...")  # Debugging output
    app.run(debug=True, host='localhost', port=5000)
