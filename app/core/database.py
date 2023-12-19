# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------

from contextlib import contextmanager
import mysql.connector
from app.core.tools import log


@contextmanager
def managed_instance(host: str, user: str, password: str, database: str):
    # Code to acquire resource, e.g.:
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        yield conn
    except Exception as e:
        raise ConnectionError(
            "[DataBase][Connection Error] Connection failed ! : " + str(e)
        )
    finally:
        if conn is not None:
            conn.commit()
            conn.close()


class Database:
    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        """
        Init database

        Args:
            host (str): db host
            user (str): db user
            password (str): db pass
            database (str): db

        """
        self.creed = {
            "host": host,
            "user": user,
            "password": password,
            "database": database,
        }
        with managed_instance(**self.creed) as conn:
            cursor = conn.cursor()

    def insert(self, table: str, values: dict, hasId: bool = False) -> dict:
        """
        Insert value in db

        Args:
            table (str): _description_
            values (dict): _description_
        
        Returns:
            dict: _description_
        """
        with managed_instance(**self.creed) as conn:

            print(
                f"INSERT INTO {table.lower()} ({','.join(values.keys())}) VALUES ({','.join('%s' for _ in values.keys())})"
            )

            try:

                cursor = conn.cursor()
                cursor.execute(
                    f"INSERT INTO {table.lower()} ({','.join(values.keys())}) VALUES ({','.join('%s' for _ in values.values())})",
                    tuple(values.values()),
                )
                conn.commit()
                if hasId:
                    values["id"] = cursor.lastrowid
                row = ",".join(list(values.keys()))
                cursor.execute(
                    f"SELECT {row} FROM {table.lower()} WHERE {' AND '.join([f'{k}=%s' for k in values.keys()])}",
                    tuple(values.values()),
                )
                res = cursor.fetchall()
                if len(res) == 0:
                    raise Exception(f"[DataBase][Insert Error] Insertion failed !")
                return dict(zip(values.keys(), res[0]))  #
            except Exception as e:
                raise Exception(f"[DataBase][Insert Error] {e}")

    def update(self, table: str, values: dict, changes: dict) -> dict:
        """
        Update value in db

        Args:
            table (str): _description_
            values (dict): _description_
        """
        with managed_instance(**self.creed) as conn:
            try:
                cursor = conn.cursor()
                print(
                    f"UPDATE {table.lower()} SET {','.join([f'{k}=%s' for k in changes.keys()])} WHERE {' AND '.join([f'{k}=%s' for k in values.keys()])}"
                )
                values_form = tuple(tuple(changes.values()) + tuple(values.values()))
                print(values_form)
                cursor.execute(
                    f"UPDATE {table.lower()} SET {','.join([f'{k}=%s' for k in changes.keys()])} WHERE {' AND '.join([f'{k}=%s' for k in values.keys()])}",
                    values_form,
                )
                conn.commit()
                # rows = ",".join(list(values.keys()))
                # cursor.execute(
                #     f"SELECT {rows} FROM {table.lower()} WHERE {' AND '.join([f'{k}=%s' for k in changes.keys()])}",tuple(changes.values())
                # )

                return ""
            except Exception as e:
                raise e
                raise Exception(f"[DataBase][Update Error] {e}")

    def select(self, table: str, values: dict, fields: dict, count: int = 1) -> dict:
        """
        Select value in db

        Args:
            table (str): _description_
            values (dict): _description_
        """
        with managed_instance(**self.creed) as conn:
            try:
                cursor = conn.cursor()

                rows = ",".join(list(fields.keys()))
                print(values)
                if values == {}:
                    cursor.execute(f"SELECT {rows} FROM {table.lower()}")

                else:
                    print(
                        f"SELECT {rows} FROM {table.lower()} WHERE { ' AND '.join([f'{k}={v}' for k,v in values.items()])}"
                    )
                    cursor.execute(
                        f"SELECT {rows} FROM {table.lower()} WHERE {' AND '.join([f'{k}=%s' for k in values.keys()])}",
                        tuple(values.values()),
                    )
                res = cursor.fetchall()

                if len(res) == 0:
                    return None

                if count == 1:
                    return dict(zip(fields.keys(), res[0]))
                else:
                    return list(dict(zip(fields.keys(), r)) for r in res)
            except Exception as e:
                raise Exception(f"[DataBase][Select Error] {e}")

    def delete(self, table, values):
        with managed_instance(**self.creed) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(
                    f"DELETE FROM {table.lower()} WHERE {' AND '.join([f'{k}=%s' for k in values.keys()])}",
                    tuple(values.values()),
                )
                conn.commit()
            except Exception as e:
                raise Exception(f"[DataBase][Delete Error] {e}")
