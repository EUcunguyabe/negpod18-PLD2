# import mysql connector


import mysql.connector
"""Mysql.connector imported"""

# create database connection
con = mysql.connector.connect(host="localhost", user="root", password="", database="health_pkd")
"""database connection created"""
# create object to help use send request and get request from database

db = con.cursor()
