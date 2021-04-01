import pandas as pd
import service

from flask import request


@service.app.route('/', methods=['GET'])
def health():
    try:
        return {
            'linear_model': str(service.linear_model.summary()),
            'dnn_model': str(service.dnn_model.summary())
        }, 200
    except Exception as e:
        return {'error': e}, 500


@service.app.route('/api/prediction/', methods=['POST'])
def prediction():
    try:
        body = request.get_json()
        model_type = body['model_type']
        features = pd.DataFrame({
            'air_humidity_100': body['features']['air_humidity_100'],
            'air_temperature_100': body['features']['air_temperature_100'],
            'atm_pressure_main': body['features']['atm_pressure_main'],
            'num_of_resets': body['features']['num_of_resets'],
            'piezo_charge': body['features']['piezo_charge'],
            'piezo_temperature': body['features']['piezo_temperature'],
        })

        if model_type == 'linear':
            labels = service.linear_model.predict(features)
        elif model_type == 'dnn':
            labels = service.dnn_model.predict(features)
        else:
            return {'error': f'invalid model_type: {model_type}'}, 400

        labels_list = [label for sublist in labels.tolist() for label in sublist]

        return {'labels': labels_list}, 200
    except KeyError:
        return {'error': 'invalid request body'}, 400
    except Exception as e:
        return {'error': e}, 501
