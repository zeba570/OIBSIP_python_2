from flask import request, jsonify
from bmi_logic import calculate_bmi, get_bmi_category
from db import insert_record, get_history
from analytics import get_statistics


def register_routes(app):

    @app.route('/calculate', methods=['POST'])
    def calculate():

        try:

            data = request.get_json()

            name = data['name']

            weight = float(data['weight'])

            height = float(data['height'])

            bmi = calculate_bmi(weight, height)

            category = get_bmi_category(bmi)

            insert_record(
                name,
                weight,
                height,
                bmi,
                category
            )

            return jsonify({

                "name": name,
                "bmi": bmi,
                "category": category
            })

        except Exception as e:

            return jsonify({
                "error": str(e)
            }), 500


    @app.route('/history', methods=['GET'])
    def history():

        data = get_history()

        return jsonify(data)
    
    @app.route('/stats', methods=['GET'])
    def stats():

        data = get_statistics()

        return jsonify(data)