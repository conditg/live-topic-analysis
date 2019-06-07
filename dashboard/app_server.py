from flask import Flask,jsonify,request
from flask import render_template
import ast
'''
This file defines a Flask app, it expects
to run in a container. It relies on a global
server state that contains the application
running status and the topics being received
for analysis.

DESCRIPTION OF OPERATION
The web app is defined in chart.html (including
Chart.js) , which is sent upon the browser
loading the root route.

Browser will continually sends an
asynchronous request for state to /getState
until the serverstate is 'running'.

While running, the data aggregator sends data
via a post request to /updateData
the browser continually sends an AJAX request
for data to /refreshData

'''

app = Flask(__name__)

serverstate = {'status':'Waiting for stream'}
alldata = {'labels':[]}

@app.route("/")
def get_chart_page():
        return render_template('chart.html')
@app.route('/refreshData')
def refresh_graph_data():
        global alldata
        return jsonify(alldata)
@app.route('/getState')
def update_server_state():
        global serverstate
        return jsonify(serverstate)
@app.route('/updateData', methods=['POST'])
def update_data():
        global alldata, serverstate
        if request.form:
            serverstate['status'] = 'Running'
        else:
            print('no data or no form')
            return "error",400
        batch = request.form.to_dict()
        print("Received: ", batch)
        #Update data with the latest batch
        serverstate['topics'] = [topic for topic in batch.keys()]
        for key in batch.keys():
            if key not in alldata.keys():
                alldata[key] = []
            alldata[key].append(batch[key])
        alldata['labels'].append('')
        return "success",201
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=9991) 


#print(batch)
#>>>{'trump':50, 'cohen':23}

#print(state)
#>>>{'trump': [50], 'cohen': [23], 'labels': ['']}
