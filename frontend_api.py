import datetime
import requests
import hashlib
# SHA hash algorithms.

# FUNCTIONS
# security(password)
# login (uid, passw)
# add_user (name, email_id, password, phone, perm)
# add_part (p_id, name, e_id, phone, events)
# add_event (name, date, time)
# get_events ()
# mark_entry (p_id, event)
# remove_event (name, date, time)
# get_report ()

url = "http://127.0.0.1:5000"


def login(uid: str, password: str) -> int:
    """
    This function is used to verify user login credentials by communicating with the server.

    :param uid: User ID used to login
    :param password: Password of the user
    :return:"1"/"2" Password match, "0" Wrong password, "-1" User dose not exists
    """
    password = security(password)
    r = requests.post(url + "/login", json={"id": uid, "password": password})
    # print(r)
    # print(type(r.text))
    # print(r.json())
    print("login", r.json()["body"])
    return r.json()["body"]["permission"]


def add_user(name: str, email_id: str, password: str, phone: int, perm: int) -> int:
    """
    Send request to add a new user to the server

    :param name: Name of the user
    :param email_id: E-mail ID of user
    :param password: Password of user
    :param phone: Phone number of user
    :param perm: Level of access provided to the user ("2" for admin, "1" for user)
    :return: "1" Added, "0" Error (Already exists)
    """
    password = security(password)
    r = requests.post(url + "/add_user", json={"name": name, "email_id": email_id, "password": password, "phone": phone, "permission": perm})
    print("add user", r.json()["body"])
    return r.json()["body"]["response"]


def add_part(p_id: str, name: str, email_id: str, phone: str, events: [str]) -> int:
    """
    Send request to add a new participant to the server

    :param p_id: ID of participant
    :param name: Name of participant
    :param email_id: E-mail ID of participant
    :param phone: Phone number of participant
    :param events: List of events
    :return: "0" some error OR no registration for this participant, "1" success, ("2"/"3"/"4") event (1/2/both) registered for this participant
    """
    r = requests.post(url + "/add_part", json={"p_id": p_id, "name": name, "email_id": email_id, "phone": phone, "events": events})
    print("add part", r.json()["body"])
    return r.json()["body"]["response"]


def add_event(name: str, date: str, time: str) -> int:
    """
    Send request to add a event to server

    :param name: Name of event
    :param date: Date of event (Format: YYYY-MM-DD)
    :param time: Time of event (Format: HH:MM)
    :return: "1" success, "0" event name exists
    """
    print(date, time)
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return 2
    try:
        datetime.datetime.strptime(time, '%H:%M')
    except ValueError:
        return 3
    time = time + ":00"
    r = requests.post(url + "/add_event", json={"name": name, "date": date, "time": time})
    print("add event", r.json()["body"])
    return r.json()["body"]["response"]


def get_events():
    """
    Send request to server for list of events

    :return: List of events
    """
    r = requests.get(url + "/get_events")
    print("get events", r.json()["body"])
    return r.json()["body"]["response"]


def mark_entry(p_id, event):
    """
    Send request to server to mark participant with "p_id" as present in specified event "event"

    :param p_id: Participant ID
    :param event: Event in which entry will be marked
    :return: "0" Not Registered, "1" Registered, "2" Already entered
    """
    r = requests.post(url + "/mark_entry", json={"p_id": p_id, "event": event})
    print("mark part", r.json()["body"])
    return r.json()["body"]["response"]


def remove_event(name, date, time):
    print("Remove", date, time)
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return 2
    try:
        datetime.datetime.strptime(time, '%H:%M')
    except ValueError:
        return 3
    time = time + ":00"
    r = requests.post(url + "/remove_event", json={"name": name, "date": date, "time": time})
    print("rem event", r.json()["body"])
    return r.json()["body"]["response"]


def get_report():
    r = requests.get(url + "/get_report")
    print("get report", r.json()["body"])
    return r.json()["body"]["response"]


def security(password: str) -> str:
    """
    This function will hash the "password" and return the hash.

    :param password: String which will be hashed
    :return: Hash of the string
    """
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
