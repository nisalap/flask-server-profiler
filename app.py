import time
from flask import Flask, jsonify, request
from werkzeug.middleware.profiler import ProfilerMiddleware

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/test', methods=['GET'])
def hello_world():
    args = dict(request.args)
    data = request.json
    print("Arguments (Key:Value)")
    for each in args:
        print(each + ":" + args[each])
    print("Data: ")
    print(data)
    response = {
        "message": "Hello World!",
        "status": "UP",
        "time": time.time()
    }
    return jsonify(response)


app.config['PROFILE'] = True
app.config["DEBUG"] = True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, profile_dir=".")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=False)
