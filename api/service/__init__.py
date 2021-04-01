import tensorflow as tf
import flask

app = flask.Flask(__name__)

dnn_model = tf.keras.models.load_model('/new_boy/dev/Desafio Técnico Dados FieldPRO/api/ml_models/dnn_model')
linear_model = tf.keras.models.load_model('/new_boy/dev/Desafio Técnico Dados FieldPRO/api/ml_models/linear_model')

print(dnn_model.summary())
print(linear_model.summary())

from service.views import *
