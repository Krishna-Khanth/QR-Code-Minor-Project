import requests
import hashlib
# SHA hash algorithms.

# login (uid, passw)
# add_user (name, email_id, password, phone, perm)
# ToDo functions
# add_part (p_id, name, e_id, phone, events)
# add_event (name, date, time)
# get_events ()
# check_part (p_id, event_id)
# ToDo List
# remove event
# Report

# security(password)

url = "http://127.0.0.1:5000"


def login(uid, password):
    password = security(password)
    r = requests.post(url + "/login", json={"id": uid, "password": password})
    print(r)
    print(type(r.text))
    print(r.json())
    print(r.json()["body"])
    return r.json()["body"]["permission"]


def add_user(name, email_id, password, phone, perm):
    password = security(password)
    r = requests.post(url + "/add_user", json={"name": name, "email_id": email_id, "password": password, "phone": phone, "permission": perm})
    print(r.json()["body"])
    return r.json()["body"]["response"]


def add_part(p_id, name, email_id, phone, events):
    r = requests.post(url + "/add_part", json={"p_id": p_id, "name": name, "email_id": email_id, "phone": phone, "events": events})
    print(r.json()["body"])


def add_event(name, date, time):
    r = requests.post(url + "/add_event", json={"name": name, "date": date, "time": time})
    print(r.json()["body"])


def get_events():
    r = requests.get(url + "/get_events")
    print(r.json()["body"])


def check_part(p_id, event_id):
    r = requests.post(url + "/check_part", json={"p_id": p_id, "event_id": event_id})
    print(r.json()["body"])


def security(password):
    password = password[::-1]
    password = hashlib.sha224(password.encode()).hexdigest()
    password = password[::-1]
    password = hashlib.sha256(password.encode()).hexdigest()
    password = password[::-1]
    return password


# if __name__ == "__main__":
#     login("admin@event.com", "Admin@123")
    # add_user(0, 0, 0, 0, 0)
    # add_part(0, 0, 0, 0, 0)
    # add_event(0, 0, 0)
    # get_events()
    # check_part("abc", 123)
