import mysql.connector
import hashlib
# SHA hash algorithms.


def db_init():
    """
    This function initializes the database and all the tables required in it.
    First Administrator is automatically added.
    Tables: User, Participant, Events, Registration.
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

    print(mydb)

    db_name = 'minor_db'

    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")
    print(mycursor)

    # Creating Database

    ls = []
    for x in mycursor:
        ls.append(x[0])

    print(ls)

    if db_name in ls:
        print("DB present")
        mycursor.execute("USE " + db_name)
    else:
        print("new db")
        mycursor.execute("CREATE DATABASE " + db_name)
        print("DB created")
        mycursor.execute("USE " + db_name)

    # Creating User Table
    mycursor.execute("SHOW TABLES")
    user_table = "user"

    ls = []
    for x in mycursor:
        ls.append(x[0])

    print(ls)

    if user_table not in ls:
        print("User not present")
        mycursor.execute("CREATE TABLE `" + db_name + "`.`user` (`User_id` INT AUTO_INCREMENT NOT NULL,`name` VARCHAR(50) NOT NULL,`Email_id` VARCHAR(45) NOT NULL,`Phone` VARCHAR(15) NOT NULL,`Password` VARCHAR(100) NOT NULL,`Permission` INT NOT NULL,PRIMARY KEY (`User_id`), UNIQUE INDEX `Email_id_UNIQUE` (`Email_id` ASC) VISIBLE,UNIQUE INDEX `User_id_UNIQUE` (`User_id` ASC) VISIBLE);")

        sql = "INSERT INTO user (User_id, name, Email_id, Phone, Password, Permission) VALUES (%s, %s, %s, %s, %s, %s)"
        password = "Admin@123"
        password = password[::-1]
        password = hashlib.sha224(password.encode()).hexdigest()
        password = password[::-1]
        password = hashlib.sha256(password.encode()).hexdigest()
        password = password[::-1]
        val = (1, "Admin", "admin@event.com", 1234567890, password, 2)
        mycursor.execute(sql, val)
        mydb.commit()

        print("User created")
    else:
        print("user exists")

    # Creating Participant Table
    mycursor.execute("SHOW TABLES")
    part_table = "participants"

    ls = []
    for x in mycursor:
        ls.append(x[0])

    print(ls)

    if part_table not in ls:
        print("part not present")
        mycursor.execute("CREATE TABLE `" + db_name + "`.`participants` (`p_id` VARCHAR(50) NOT NULL,`name` VARCHAR(50) NOT NULL,`Email_id` VARCHAR(45) NOT NULL,`Phone` VARCHAR(15) NOT NULL,PRIMARY KEY (`p_id`), UNIQUE INDEX `phone_UNIQUE` (`phone` ASC) VISIBLE,UNIQUE INDEX `idparticipants_UNIQUE` (`p_id` ASC) VISIBLE);")

        print("part created")
    else:
        print("part exists")

    # Creating Events Table
    mycursor.execute("SHOW TABLES")
    event_table = "events"

    ls = []
    for x in mycursor:
        ls.append(x[0])

    print(ls)

    if event_table not in ls:
        print("event not present")
        mycursor.execute("CREATE TABLE `" + db_name + "`.`events` (`event_id` INT NOT NULL AUTO_INCREMENT,`name` VARCHAR(50) NOT NULL,`date` DATE NOT NULL,`time` TIME NOT NULL,PRIMARY KEY (`event_id`),UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,UNIQUE INDEX `event_id_UNIQUE` (`event_id` ASC) VISIBLE);")

        print("event created")
    else:
        print("event exists")

    # Creating Registration Table
    mycursor.execute("SHOW TABLES")
    reg_table = "registration"

    ls = []
    for x in mycursor:
        ls.append(x[0])

    print(ls)

    if reg_table not in ls:
        print("reg not present")
        mycursor.execute("CREATE TABLE `" + db_name + "`.`registration` (`r_id` INT NOT NULL AUTO_INCREMENT,`p_id` VARCHAR(50) NOT NULL,`event_id` INT NOT NULL,`present` INT NOT NULL, PRIMARY KEY (`r_id`),UNIQUE INDEX `r_id_UNIQUE` (`r_id` ASC) VISIBLE,INDEX `p_id_idx` (`p_id` ASC) VISIBLE,INDEX `event_id_idx` (`event_id` ASC) VISIBLE,CONSTRAINT `p_id`  FOREIGN KEY (`p_id`)  REFERENCES `" + db_name + "`.`participants` (`p_id`)  ON DELETE NO ACTION  ON UPDATE NO ACTION,CONSTRAINT `event_id`  FOREIGN KEY (`event_id`)  REFERENCES `" + db_name + "`.`events` (`event_id`)  ON DELETE NO ACTION  ON UPDATE NO ACTION);")

        print("reg created")
    else:
        print("reg exists")
    print(mycursor)


# if __name__ == "__main__":
#     db_init()
#     print("--------------------------------------------------")
