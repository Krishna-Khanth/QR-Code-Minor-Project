import mysql.connector

# sql_connect ()
# add_event (name, date, time)
# add_participant (p_id, name, email, phone)
# add_user (name, email, phone, passw, perm)
# add_reg (p_id, event_id)
# get_event_id (name)
# get_events ()
# get_user ()
# get_reg (p_id, event_id)
# get_pid (phone)
# remove_event (name, date, time)
# get_report ()
# mark_entry (p_id, event_id)
# check_part (p_id)


def sql_connect():
    """
    Make a connection to the database.

    :return: database name, Cursor object of database, connector of database.
    """
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="minor",
            password="1234"
        )
    except:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="pass"
        )
    mycursor = mydb.cursor()
    db_name = "minor_db"
    return db_name, mycursor, mydb


def add_event(name: str, date: str, time: str) -> int:
    """
    Command database to add an event.

    :param name: Name of event.
    :param date: Date of event.
    :param time: Time of event.
    :return: "1" success, "0" event name exists.
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    # Date "yyyy-mm-dd" Time "hh:mm:ss"
    try:
        sql = "INSERT INTO events (name, date, time) VALUES (%s, %s, %s)"
        val = (name, date, time)
        mycursor.execute(sql, val)

        mydb.commit()
        print(name, date, time, "inserted")
        return 1
    except:
        print("Error: db_op \nName already exists")
        return 0


def add_participant(p_id: str, name: str, email: str, phone: str) -> int:
    """
    Command database to add a new participant.

    :param p_id: Participant ID.
    :param name: Participant name.
    :param email: Participant E-mail ID.
    :param phone: Participant phone number.
    :return: "0" some error, "1" success.
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    try:
        sql = "INSERT INTO participants (p_id, name, email_id, phone) VALUES (%s, %s, %s, %s)"
        val = (p_id, name, email, phone)
        mycursor.execute(sql, val)

        mydb.commit()
        print(name, email, phone, "inserted")
        return 1
    except:
        print("Error: db_op \nParticipant already exists")
        return 0


def add_user(name: str, email: str, phone: str, passw: str, perm: int) -> int:
    """
    Command database to add a new user.

    :param name: Name of user.
    :param email: E-mail ID of user.
    :param passw: Hash of password of new user.
    :param phone: Phone number of new user.
    :param perm: Permission level provided to user.
    :return: "1" if added, "0" Error (user already exists).
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)
    phone = str(phone)
    passw = str(passw)

    try:
        sql = "INSERT INTO user (name, email_id, phone, password, permission) VALUES (%s, %s, %s, %s, %s)"
        val = (name, email, phone, passw, perm)
        mycursor.execute(sql, val)

        mydb.commit()
        print(name, email, phone, passw, perm, "inserted")
        return 1
    except:
        print("Error: db_op - E-mail already exists.")
        return 0


def add_reg(p_id: str, event_id: str) -> int:
    """
    Command database to register a participant in an event.

    :param p_id: Participant ID.
    :param event_id: Event ID.
    :return: "0" some error, "1" success.
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    try:
        sql = "INSERT INTO registration (p_id, event_id, present) VALUES (%s, %s, %s)"
        val = (p_id, event_id, 1)
        mycursor.execute(sql, val)
        mydb.commit()
        print(p_id, event_id, "inserted")
        return 1
    except:
        print("db_op : p_id or event_id incorrect")
        return 0


def get_event_id(name: str) -> int:
    """
    Retrieve event ID from database using the event name.

    :param name: Event name.
    :return: Event ID.
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    sql = "SELECT event_id FROM events WHERE name = \"" + name + "\""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print(myresult)
    return myresult


def get_events() -> [str]:
    """
    Retrieve List of events from database.

    :return: List of events.
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    mycursor.execute("SELECT name FROM events")
    myresult = mycursor.fetchall()
    print(myresult)
    return myresult


def get_user() -> [[str]]:
    """
    Retrieve e-mail id, password and permission level of user from database.

    :return: List of e-mail id, password and permission level of all users.
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    mycursor.execute("SELECT email_id, password, permission FROM user")
    myresult = mycursor.fetchall()
    print("db - login working" if len(myresult) > 0 else "db - No login data")
    return myresult


def get_reg(p_id: str, event_id: str) -> int:
    """
    Retrieve entry detail of a participant in a particular event.

    :param p_id: Participant ID.
    :param event_id: Event ID.
    :return: "1" Not Entered, "2" Entered, "0" Dose not exists.
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)
    event_id = str(event_id)
    print("db get reg pid eid", p_id, event_id)
    try:
        sql = "SELECT present FROM registration WHERE p_id = %s AND event_id = %s"
        val = (p_id, event_id)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        print("db get reg", myresult)
        return myresult[0][0]
    except:
        print("db_op - Dose not exist")
        return 0


def get_pid(phone: str) -> str:
    """
    Retrieve participant id of a participant from phone number.
    :param phone: Phone number of participant.
    :return: Participant ID.
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)
    phone = str(phone)

    mycursor.execute("SELECT p_id FROM participants WHERE phone = " + phone)
    myresult = mycursor.fetchall()
    print(myresult[0][0])
    return myresult[0][0]


def remove_event(name: str, date: str, time: str) -> int:
    """
    Command database to delete an event.

    :param name: Name of event.
    :param date: Date of event.
    :param time: Time of event.
    :return: "1" success, "0" event participant registered, "4" wrong event details.
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    # Date "yyyy-mm-dd" Time "hh:mm:ss"
    try:
        sql = "DELETE FROM events WHERE name = %s AND date = %s AND time = %s"
        val = (name, date, time)
        mycursor.execute(sql, val)
        mydb.commit()
        print("row = ", mycursor.rowcount)
        if mycursor.rowcount == 0:
            print("no change")
            return 4
        print(name, date, time, "deleted")
        return 1
    except:
        print("Error: db_op -  Someone is registered")
        return 0


def get_report() -> [[str]]:
    """
    Retrieve participant details and events they registered in from database.

    :return: List of participant details.
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    sql = "SELECT `minor_db`.`participants`.*, GROUP_CONCAT(`minor_db`.`events`.name, `minor_db`.`registration`.present) as \"events\" FROM ((`minor_db`.`participants` INNER JOIN `minor_db`.`registration` ON `minor_db`.`participants`.p_id = `minor_db`.`registration`.p_id) INNER JOIN `minor_db`.`events` ON `minor_db`.`events`.event_id = `minor_db`.`registration`.event_id) group by p_id;"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print(myresult)
    return myresult


def mark_entry(p_id: str, event_id: str) -> int:
    """
    Command database to mark a participant entry in a event.

    :param p_id: Participant ID.
    :param event_id: Event ID.
    :return: "0" Not Registered, "1" Registered, "2" Entered.
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    sql = "UPDATE `minor_db`.`registration` SET `present` = '2' WHERE p_id = %s AND event_id = %s"
    val = (p_id, event_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print("entry row = ", mycursor.rowcount)


def check_part(p_id: str) -> int:
    """
    Retrieve all details of participant from database.

    :param p_id: Participant ID.
    :return: List of details of participant.
    """
    db_name, mycursor, mydb = sql_connect()
    mycursor.execute("USE " + db_name)

    sql = "SELECT * FROM participants WHERE p_id = \"" + p_id + "\""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print(myresult)
    print("check_part-", mycursor.rowcount)
    return mycursor.rowcount


# if __name__ == "__main__":
    # add_event("jkl", "2020-09-30", "10:10")
    # add_participant("54321", "sharad", "mp@gmail.in", 1234567890)
    # add_user("sharad", "mp@gmail.in", 1234567890, "abc", 2)
    # add_reg(54321, 1)
    # get_events()
    # get_user()
    # get_reg("dummy1-1111111111", "1")
    # mark_entry("dummy1-1111111111", "1")
    # get_report()
    # check_part("dummy5-1111111111")
