from flask import Flask,jsonify,request
from flask_cors import CORS
import re
import base64
app= Flask(__name__)
CORS(app)

@app.route('/upload_file',methods=['POST'])
def upload_file():
  if 'file' not in request.files:
    return jsonify({
      "message": "No se pudo cargar el archivo"
    })
  file = request.files['file']
  file_contents=file.read().decode('utf-8')
  print(file_contents)
  return jsonify({
      "message": "El archivo fue cargado"
    })  

@app.route('/flask_response',methods=['GET'])
def get_response_from_flask():
  response_data={"message":"PRUEBA 1"}
  return jsonify(response_data)

@app.route('/flask_response2',methods=['GET'])
def get_response_from_flask2():
  response_data={"message":"PRUEBA 2"}
  return jsonify(response_data)


if __name__=="__main__":
  app.run(threaded=True,port=5000,debug=True)




