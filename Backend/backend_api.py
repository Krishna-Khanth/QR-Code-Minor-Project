
# A very simple Flask Hello World app for you to get started with...
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

try:
    import Backend.manage_op as op
except:
    import manage_op as op

app = Flask(__name__)
CORS(app)

# login
# add_user
# add_part
# add_event
# get_events
# mark_entry
# remove_event
# get_report


@app.route('/')
def hello_world():
    return 'Hello from Flask! This is a test site'


@app.route('/login', methods=["Post"])
def login():
    req_data = request.get_json()
    # permission = "Custom Response"
    id = req_data["id"]
    passw = req_data["password"]
    print("b api", id, passw)

    # permission = id + passw
    # "1"/"2" Password match, "0" Wrong password, "-1" User dose not exists
    permission = op.login(uid=id, passw=passw)

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "permission": permission
        }
    })


@app.route('/add_user', methods=["Post"])
def add_user():
    req_data = request.get_json()
    response = "Custom Response"
    e_id = req_data["email_id"]
    passw = req_data["password"]
    phone = req_data["phone"]
    name = req_data["name"]
    perm = req_data["permission"]
    print("b api", name, e_id, phone, passw, perm)

    # "1" if added, "0" if exists
    response = op.add_user(name=name, email_id=e_id, phone=phone, perm=perm, password=passw)

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


@app.route('/add_part', methods=["Post"])
def add_part():
    req_data = request.get_json()
    response = "Custom Response"
    e_id = req_data["email_id"]
    events = req_data["events"]
    p_id = req_data["p_id"]
    phone = req_data["phone"]
    name = req_data["name"]
    print("b api", p_id, name, e_id, phone, events)

    # "0" some error / no registration for this participant, "1" success,
    # ("2"/"3"/"4") event (1/2/both) registered for this participant
    response = op.add_part(p_id=p_id, name=name, email=e_id, phone=phone, events=events)

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


@app.route('/add_event', methods=["Post"])
def add_event():
    req_data = request.get_json()
    response = "Custom Response"
    date = req_data["date"]
    time = req_data["time"]
    name = req_data["name"]
    print("b api", name, date, time)

    # "1" success, "0" event name exists
    response = op.add_event(name=name, date=date, time=time)

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


@app.route('/get_events')
def get_events():
    response = "Custom Response"

    # list of tupple(event_id and name)
    response = op.get_events()

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


@app.route('/mark_entry', methods=["Post"])
def mark_entry():
    req_data = request.get_json()
    response = "Custom Response"
    p_id = req_data["p_id"]
    event = req_data["event"]
    print("b api", p_id, event)

    # "0" Not Registered, "1" Registered, "2" Entered
    response = op.mark_entry(p_id=p_id, event=event)

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


@app.route('/remove_event', methods=["Post"])
def remove_event():
    req_data = request.get_json()
    response = "Custom Response"
    date = req_data["date"]
    time = req_data["time"]
    name = req_data["name"]
    print("b api", name, date, time)

    # "1" success, "0" event participant registered, "4" wrong event details
    response = op.remove_event(name=name, date=date, time=time)

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


@app.route('/get_report')
def get_report():
    response = "Custom Response"

    # list of tupple(event_id and name)
    response = op.get_report()

    return jsonify({
        "method": "POST",
        "headers": {
            "content-type": "application/json"
        },
        "body": {
            "response": response
        }
    })


# app.run(debug=True)
app.run()
