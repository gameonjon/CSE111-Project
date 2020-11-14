import sqlite3
from sqlite3 import Error
import time

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    return conn


def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create tables")


            #==================================
            #STILL NEED CONNECTION TO SOME 
    try:
        sql = """CREATE TABLE Games (
                    g_title varchar(30) NOT NULL,
                    g_year DATE NOT NULL,
                    g_genre varchar(15) NOT NULL,
                    g_exkey decimal(5,0) NOT NULL,
                    g_pubkey decimal(12,0) NOT NULL,
                    g_devkey decimal(12,0) NOT NULL
                    )"""
        _conn.execute(sql)

        sql = """CREATE TABLE Platform (
                    pf_system varchar(25) NOT NULL,
                    pf_exkey decimal(5,0) NOT NULL,
                    pf_exclusive boolean NOT NULL
                    )"""
        _conn.execute(sql)

        sql = """CREATE TABLE Reviews (
                    r_gameTitle varchar(30) NOT NULL,
                    r_rating decimal(2,1) NOT NULL,
                    r_resource varchar(25) NOT NULL,
                    r_comment VARCHAR(50) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE Publisher (
                    p_name varchar(30) NOT NULL,
                    p_pubkey decimal(12,0)
                )"""
        _conn.execute(sql)

        sql = """CREATE TABLE Developer (
                    d_name varchar(30) NOT NULL,
                    d_devkey decimal(12,0)
                )"""
        _conn.execute(sql)

        sql = """CREATE TABLE GamePlay (
                    gp_gameTitle varchar(30) NOT NULL,
                    gp_url varchar(15) NOT NULL,
                    gp_platform varchar(30) NOT NULL
                )"""
        _conn.execute(sql)

        _conn.commit()
        print("success")
    
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def dropTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    try: 
        sql = "DROP TABLE Games"
        _conn.execute(sql)

        sql = "DROP TABLE Platform"
        _conn.execute(sql)

        sql = "DROP TABLE Reviews"
        _conn.execute(sql)

        sql = "DROP TABLE Publisher"
        _conn.execute(sql)

        sql = "DROP TABLE Developer"
        _conn.execute(sql)

        sql = "DROP TABLE GamePlay"
        _conn.execute(sql)

        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTable_Games(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")

    try:

        games = [               #(title, year, genre, exkey, pubkey, devkey)

            #Platform:
            # ps4, xbox1, xbox360, MSW, Mac OS, Linux
            ("Rise of the Tomb Raider", '2016-02-09', "action-adventure", 11, 10001, 20001),
            #Platform: ps4, xbox1, MSW
            ("Star Wars: Jedi Fallen Order",'2019-11-15', "action-adventure", 11, 10004, 20005),
            #Platform: ps4, xbox1, MSW
            ("Star Wars: BattleFront 2", '2017-11-17', "shooter", 11, 10004, 20006),
            #Platform: ps4, MSW
            ("Death Stranding", '2019-11-08', "action", 5, 10006, 20009),
            #Platform: ps4, nintendo switch, xbox 1, msw
            ("Overwatch", "2016-05-24", "shooter", 13, 10007, 20010),
            #Platform: ps4, xbox1, msw, nintendo switch
            ("Bioshock: The Collection", '2016-09-13', "shooter", 13, 10008, 20012),
            #Platform: ps4, xbox1, msw, linux, classic Mac os
            ("Dying Light", '2015-01-26', "action", 11, 10010, 20017), 
            #Platform: ps4, xbox1, ps3, xbox360, msw
            ("Battlefield 4", '2013-10-29', "shooter", 11, 10004, 20006),
            #Platform: ps4, xbox1, msw
            ("Call of Duty: Modern Warfare Remastered", '2016-11-04', "shooter", 11, 10012, 20018),
            #Platform: ps4, xbox1, msw
            ("Tom Clancy's Ghost Recon", '2017-03-07', "tactical shooter", 11, 10013, 20021),
            #Platform: ps4 
            ("Killzone Shadow Fall", '2013-11-15', "shooter", 1, 10005, 20024),
            #Platform: ps4
            ("The Last of Us Remastered", '2014-07-29', "survival-horror", 1, 10005, 20025),
            #Platform: ps4, msw, xbox1
            ("Star Wars: Battlefront", '2017-11-17', "shooter", 11, 10004, 20006),
            #Platform: ps4, msw
            ("Horizor Zero Dawn", '2017-02-28', "action", 5, 10005, 20024),
            #Platform: ps4, xbox1, msw
            ("Battlefield 1", '2016-10-21', "shooter", 11, 10004, 20006),
            #Platform: ps4, xbox1, msw
            ("Need for Speed", '2015-11-03', "racing", 11, 10004, 20026),
            #Platform: ps4
            ("Spider-Man", '2018-09-07', "action-adventure", 1, 10005, 20027),
            #Platform: ps4, xbox1, msw
            ("Call of Duty: Modern Warfare", '2019-08-23', "shooter", 11, 10012, 20018)


        ]
        sql = "INSERT INTO Games VALUES(?, ?, ?, ?, ?, ?)"
        _conn.executemany(sql, games)

        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def populateTable_DevPub(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Developer and Publisher tables:")

    try: 
        pub = [
            ("Square Enix", 10001),
            ("Feral Interactive", 10002),
            ("Xbox Game Studios", 10003),
            ("Electronic Arts", 10004),
            ("Sony Interactive Entertainment", 10005),
            ("505 Games", 10006), 
            ("Blizzard Entertainment", 10007), 
            ("2K Games", 10008),
            ("Take-Two Interactive", 10009),
            ("Techland", 10010),
            ("Warner Bros. Interactive Entertainment", 10011),
            ("Activision", 10012),
            ("Ubisoft", 10013),
            ("Gameloft", 10014),
            ("Aspyr", 10015),
            ("Frontier Groove, Inc.", 10016)

        ]
        sql = "INSERT INTO Publisher Values(?, ?)"
        _conn.executemany(sql, pub)

        dev = [
            ("Crystal Dynamics", 20001),
            ("Eidos-Montreal", 20002),
            ("Feral Interactive", 20003),
            ("Cameron Suey", 20004),
            ("Respawn Entertainment", 20005),
            ("DICE", 20006),
            ("Motive Studios", 20007),
            ("Criterion Software", 20008),
            ("Kojima Productions", 20009),
            ("Blizzard Entertainment", 20010),
            ("Iron Galaxy", 20011),
            ("Irrational Games", 20012),
            ("2K Marin", 20013),
            ("2K Australia", 20014),
            ("Blind Squirrel Games", 20015),
            ("Digital Extremes", 20016),
            ("Techland", 20017),
            ("Infinity Ward", 20018),
            ("Raven Software", 20019),
            ("Beenox", 20020),
            ("Ubisoft", 20021),
            ("Ubisoft Paris", 20022),
            ("Red Storm Entertainment", 20023),
            ("Guerrilla Games", 20024),
            ("Naughty Dog", 20025), 
            ("Electronic Arts", 20026),
            ("Insomniac Games", 20027),
            ("Sledgehammer Games", 20028)


        ]
        sql = "INSERT INTO Developer Values(?, ?)"
        _conn.executemany(sql, dev)

        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")

def populate_Platforms(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Platforms")

    try: 
        exclusive = [ #platform(system, exkey, exclusive)
            ("Playstation", 1, 1),
            ("Xbox", 2, 1),
            ("PC", 3, 1),
            ("Nintendo Switch", 4, 1),

            ("PC\nPlaystation", 5, 0),
            ("PC\nXbox", 6, 0),
            ("PC\nNintendo Switch", 7, 0),
            ("Playstation\nXbox", 8, 0),
            ("Playstation\nNintendo Switch", 9, 0),
            ("Xbox\nNintendo Switch", 10, 0),

            ("PC\nPlaystation\nXbox", 11, 0),
            ("Playstation\nXbox\nNintendo Switch", 12, 0),
            ("PC\nPlaystation\nXbox\nNintendo Switch", 13, 0),
            ("PC\nPlaystation\nNintendo Switch", 14, 0),
            ("PC\nXbox\nNintendo Switch", 15, 0)
            
        ]
        sql = "INSERT INTO Platform VALUES(?, ?, ?)"
        _conn.executemany(sql, exclusive)

        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    
def populate_Reviews(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Platforms")

    try: 
        review = [ #Revews(gameTitle, rating, resource, comment)
                        # (varchar(30), decimal, varchar, varchar)
            ("The Last of Us Remastered", 10, "IGN", "With The Last of Us: Remastered, PlayStation 3's best game just became PlayStation 4's, too."),
            ("The Last of Us Remastered", 9, "Metro GameCentral", "Still a stunning achievement in both storytelling and third person adventure, and although this is the definitive version the differences are still minor."),
            ("The Last of Us Remastered", 10, "Game Informer", "The punishing world dares you to press on, and the story is an emotional punch to the gut. In short, this is one of the best video games ever made")
            
        ]
        sql = "INSERT INTO Reviews VALUES(?, ?, ?, ?)"
        _conn.executemany(sql, review)

        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def populate_gamePlay(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate GamePlay")

    try: # GamePlay(gameTitle, website, platform)
        gamePlay = [
            ("Call of Duty: Modern Warfare", "https://www.twitch.tv/directory/game/Call%20Of%20Duty%3A%20Modern%20Warfare", "Twitch"),
            ("Call of Duty: Modern Warfare", "https://www.youtube.com/results?search_query=call+of+duty+modern+warfare", "Youtube"),
            ("Overwatch", "https://www.twitch.tv/directory/game/Overwatch", "Twitch"),
            ("Overwatch", "https://www.youtube.com/results?search_query=overwatch", "Youtube"),
            ("The Last of Us Remastered", "https://www.twitch.tv/directory/game/The%20Last%20of%20Us", "Twitch"),
            ("The Last of Us Remastered", "https://www.youtube.com/results?search_query=the+last+of+us+remastered", "Youtube")
        ]
        sql = "INSERT INTO GamePlay Values(?, ?, ?)"
        _conn.executemany(sql, gamePlay)

        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    
def main():
    database = r"data.sqlite"
    conn = openConnection(database)
    with conn:
        createTables(conn)
        populateTable_Games(conn)
        populateTable_DevPub(conn)
        populate_Platforms(conn)
        populate_Reviews(conn)
        populate_gamePlay(conn)
        #dropTables(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()