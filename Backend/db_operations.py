import mysql.connector

# add_event (name, date, time)
# add_participant (p_id, name, email, phone)
# add_user (name, email, phone, passw, perm)
# add_reg (p_id, event_id)
# get_events ()
# get_user ()
# get_reg (p_id, event_id)
# get_pid (phone)


def add_event(name, date, time):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="minor",
        password="1234"
    )
    mycursor = mydb.cursor()
    db_name = "minor_db"
    mycursor.execute("USE " + db_name)

    # Date "yyyy-mm-dd" Time "hh:mm:ss"
    time = time + ":00"
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


def add_participant(p_id, name, email, phone):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="minor",
        password="1234"
    )
    mycursor = mydb.cursor()
    db_name = "minor_db"
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


def add_user(name, email, phone, passw, perm):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="minor",
        password="1234"
    )
    mycursor = mydb.cursor()
    db_name = "minor_db"
    mycursor.execute("USE " + db_name)

    try:
        sql = "INSERT INTO user (name, email_id, phone, password, permission) VALUES (%s, %s, %s, %s, %s)"
        val = (name, email, phone, passw, perm)
        mycursor.execute(sql, val)

        mydb.commit()
        print(name, email, phone, passw, perm, "inserted")
        return 1
    except:
        print("Error: db_op \nEmail already exists.")
        return 0


def add_reg(p_id, event_id):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="minor",
        password="1234"
    )
    mycursor = mydb.cursor()
    db_name = "minor_db"
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


def get_events():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="minor",
        password="1234"
    )
    mycursor = mydb.cursor()
    db_name = "minor_db"
    mycursor.execute("USE " + db_name)

    mycursor.execute("SELECT event_id, name FROM events")
    myresult = mycursor.fetchall()
    print(myresult)
    return myresult


def get_user():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="minor",
        password="1234"
    )
    mycursor = mydb.cursor()
    db_name = "minor_db"
    mycursor.execute("USE " + db_name)

    mycursor.execute("SELECT email_id, password, permission FROM user")
    myresult = mycursor.fetchall()
    print(myresult)

    return myresult


def get_reg(p_id, event_id):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="minor",
        password="1234"
    )
    mycursor = mydb.cursor()
    db_name = "minor_db"
    mycursor.execute("USE " + db_name)
    event_id = str(event_id)

    try:
        mycursor.execute("SELECT present FROM registration WHERE p_id = \"" + p_id + "\" AND event_id = " + event_id)
        myresult = mycursor.fetchall()
        print(myresult)
        print(len(myresult))
        return myresult[0][0]
    except:
        print("db_op - Dose not exist")
        return 0


def get_pid(phone):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="minor",
        password="1234"
    )
    mycursor = mydb.cursor()
    db_name = "minor_db"
    mycursor.execute("USE " + db_name)
    phone = str(phone)

    mycursor.execute("SELECT p_id FROM participants WHERE phone = " + phone)
    myresult = mycursor.fetchall()
    print(myresult)
    print(len(myresult))
    print(myresult[0][0])


if __name__ == "__main__":
    # add_event("jkl", "2020-09-30", "10:10")
    # add_participant("54321", "sharad", "mp@gmail.in", 1234567890)
    # add_user("sharad", "mp@gmail.in", 1234567890, "abc", 2)
    # add_reg(54321, 1)
    get_events()
    get_user()
    # get_reg("54321", 1)
