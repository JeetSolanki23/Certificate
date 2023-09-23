from flask import Flask, request, jsonify


import json



app = Flask(__name__)



@app.route('/')

def home():

    return "Namaste"



@app.route('/predict', methods=["GET","POST"])

def predict():

	

    query = request.json['query'].lower()

    apps_list = request.json['apps_list']





    # result = {'response' : 'it\'s done'}

    result = varify(query,apps_list)

 



    if result['Category'] != 'open app':

        ans = ReplyBrain(query)

        if "'" not in ans:

            result = "{'Category':'reply','speak': '"+ans+"'}"

        else:

            result = '{"Category":"reply","speak": "'+ans+'"}'



        return result

        # return jsonify(json.loads(result))

    else:

        return jsonify(result)

if __name__=='__main__':

    app.run(debug=True, host="0.0.0.0")
