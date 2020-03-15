#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mysql.connector

def ConnetDb(host,user,passwd):
    connection=mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database="OA"
        )
    
    return connection