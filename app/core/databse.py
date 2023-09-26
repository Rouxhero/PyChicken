# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
#-------------------

import mysql.connector

class Database:

    def __init__(self,host:str,user:str,password:str,database:str)->None:
        """
        Init database

        Args:
            host (str): db host
            user (str): db user
            password (str): db pass
            database (str): db

        """        
        try:
            self.conn = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
            )
            self.cursor = self.conn.cursor()
            self.isConnected = True
        except Exception as e:
            # raise Exception("[DataBase][Connection Error] Connection failed !")
            pass
        

    def insert(self,table:str,values:dict)->None:
        """
        Insert value in db

        Args:
            table (str): _description_
            values (dict): _description_
        """        
        print(table,values)