from flask import Flask, jsonify
import string
import requests
import psutil as ps
app = Flask(__name__)

@app.route('/<message>', methods=['GET','POST'])
def main(message):
    type_msg = message.split(':')
    if type_msg[0]=='tmp':
        return jsonify({
            "sended": message,
            "response": ps.cpu_percent(),
        })
    else:
        return jsonify({
            "sended": message,
            "response": "Quantidade de letras 'a' :%d"%type_msg[1].lower().count('a'),
        })
if __name__ == '__main__':
    app.run(debug = True, host = '10.180.47.54', port = 5002)
