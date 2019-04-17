import requests, string, asyncio, time
from flask import Flask, jsonify
from threading import Thread


app = Flask(__name__)

@app.route('/mid/<name>', methods = ['GET','POST'])
def main(name):
    servA, servB =  requests.post("http://10.180.61.164:5001/tmp:"), requests.post("http://10.180.45.140:5002/tmp:")
    respA, respB = servA.json()['response'],servB.json()['response']
    if respA <= respB:
        servA =  requests.post("http://10.180.61.164:5001/msg:%s" % (name))
        return jsonify({
            "Escolhido Server A":  servA.json()['response'],
        })
    else:
        servB =  requests.post("http://10.180.45.140:5002/msg:%s" % (name))
        return jsonify({
            "Escolhido Server B":  servB.json()['response'],
        })

if __name__ == '__main__':
    app.run(threaded = True, debug = True, host='127.0.0.1', port = 4000)
