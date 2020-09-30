import requests

# login (uid, passw)
# add_user (name, email_id, password, phone, perm)
# add_part (p_id, name, e_id, phone, events)
# add_event (name, date, time)
# get_events ()
# check_part (p_id, event_id)


def login(uid, password):
    r = requests.post("http://127.0.0.1:5000/login", json={"id": uid, "password": password})
    print(r)
    print(type(r.text))
    print(r.json())
    print(r.json()["body"])
    return r.json()["body"]["permission"]


def add_user(name, email_id, password, phone, perm):
    r = requests.post("http://127.0.0.1:5000/add_user", json={"name": name, "email_id": email_id, "password": password, "phone": phone, "permission": perm})
    print(r.json()["body"])


def add_part(p_id, name, email_id, phone, events):
    r = requests.post("http://127.0.0.1:5000/add_part", json={"p_id": p_id, "name": name, "email_id": email_id, "phone": phone, "events": events})
    print(r.json()["body"])


def add_event(name, date, time):
    r = requests.post("http://127.0.0.1:5000/add_event", json={"name": name, "date": date, "time": time})
    print(r.json()["body"])


def get_events():
    r = requests.get("http://127.0.0.1:5000/get_events")
    print(r.json()["body"])


def check_part(p_id, event_id):
    r = requests.post("http://127.0.0.1:5000/check_part", json={"p_id": p_id, "event_id": event_id})
    print(r.json()["body"])


# if __name__ == "__main__":
    # login("123", "asdf")
    # add_user(0, 0, 0, 0, 0)
    # add_part(0, 0, 0, 0, 0)
    # add_event(0, 0, 0)
    # get_events()
    # check_part("abc", 123)
