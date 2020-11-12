import sqlite3
from sqlite3 import Error

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
                    g_exclusive boolean,
                    g_pubkey decimal(12,0),
                    g_devkey decimal(12,0),
                    )"""
        _conn.execute(sql)

        sql = """CREATE TABLE Platform (
                    pf_system varchar(12) NOT NULL
                    pf_exclusive boolean)"""
        _conn.execute(sql)

        sql = """CREATE TABLE Reviews (
                    r_rating decimal(5,0) NOT NULL,
                    r_comment VARCHAR(50) NOT NULL,
                    r_resource varchar(25) NOT NULL)"""
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

        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")

    
