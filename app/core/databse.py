# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
#-------------------

import mysql.connector
from app.core.tools import log



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
        self.isConnected = False
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
            raise Exception("[DataBase][Connection Error] Connection failed ! : "+str(e))

        

    def insert(self,table:str,values:dict)->dict:
        """
        Insert value in db

        Args:
            table (str): _description_
            values (dict): _description_
        
        Returns:
            dict: _description_
        """        
        if self.isConnected:
            print(f"INSERT INTO {table.lower()} ({','.join(values.keys())}) VALUES ({','.join('%s' for x in values.keys())})")
            print(tuple(values.values()))
            try :
                self.cursor.execute(f"INSERT INTO {table.lower()} ({','.join(values.keys())}) VALUES ({','.join('%s' for x in values.values())})",tuple(values.values()))
                self.conn.commit()
                self.cursor.execute(f"SELECT * FROM {table.lower()} WHERE id={self.cursor.lastrowid}")
                return self.cursor.fetchone()
            except Exception as e:
                raise Exception(f"[DataBase][Insert Error] {e}")
            
    def update(self,table:str,values:dict)->dict:
        """
        Update value in db

        Args:
            table (str): _description_
            values (dict): _description_
        """        
        if self.isConnected:
            try :
                self.cursor.execute(f"UPDATE {table.lower()} SET {','.join([f'{k}=%s' for k in values.keys()])} WHERE id=%s",tuple(values.values()))
                self.conn.commit()
                self.cursor.execute(f"SELECT * FROM {table.lower()} WHERE id={self.cursor.lastrowid}")
                return self.cursor.fetchone()
            except Exception as e:
                raise Exception(f"[DataBase][Update Error] {e}")
       