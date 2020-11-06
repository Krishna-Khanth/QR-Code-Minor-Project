try:
    import Backend.db_operations as db
    import Backend.database as db_init
except:
    import database as db_init
    import db_operations as db

# login (uid, passw)
# add_user (name, email_id, password, phone, perm)
# add_part (p_id, name, e_id, phone, events)
# add_event (name, date, time)
# get_events ()
# check_part (p_id, event_id)
# remove_event (name, date, time)
# get_report ()


def login(uid, passw):
    try:
        users = db.get_user()
    except:
        print("user table not exists")
        db_init.db_init()
        users = db.get_user()
        print("user table created")

    for i in users:
        if i[0] == uid:
            # User email exists
            if passw == i[1]:
                # "1"/"2" Password match
                return i[2]
            # "0" Wrong password
            return 0
    # "-1" User dose not exists
    return -1


def add_user(name, email_id, password, phone, perm):
    success = db.add_user(name=name, email=email_id, phone=phone, passw=password, perm=perm)
    # "1" if added, "0" if exists
    return success


def add_part(p_id, name, email, phone, events):

    status = db.add_participant(p_id=p_id, name=name, email=email, phone=phone)

    if status == 0:
        # User exists
        print("manage_op - Participant exists")
        p_id = db.get_pid(phone)

    for i in events:
        print("for event = ", i)
        e_id = db.get_event_id(i)
        print("event id = ", e_id[0][0])
        resp = db.add_reg(p_id=p_id, event_id=e_id[0][0])
        if resp == 0:
            print("Error - manage_op, add_part")
            return 0
    # "0" some error, "1" success
    return 1


def add_event(name, date, time):
    resp = db.add_event(name=name, date=date, time=time)
    # "1" success, "0" event name exists
    return resp


def get_events():
    events = db.get_events()
    # list of tupple(name)
    return events


def check_part(p_id, event):
    event_id = db.get_event_id(event)
    print("mop check - ", event_id[0][0])
    resp = db.get_reg(p_id=p_id, event_id=event_id[0][0])
    if resp == 1:
        db.mark_entry(p_id=p_id, event_id=event_id[0][0])
    # "0" Not Registered, "1" Registered, "2" Entered
    return resp


def remove_event(name, date, time):
    resp = db.remove_event(name=name, date=date, time=time)
    # "1" success, "0" event participant registered, "4" wrong event details
    return resp


def get_report():
    return db.get_report()
