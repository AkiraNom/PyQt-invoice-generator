from os.path import join
from glob import glob
import pandas as pd
import sqlite3
from pathlib import Path

class DataBaseConnect:
    def __init__(self):
        self.db_folder = "./db"
        self.db_path = f"{self.db_folder}/invoice_db.db"
        self.table_name = "clients"
        self.connection = None
        self.cursor = None

        self.csv_folder = "./csv"
        self.get_csv_file_path()

        self.init_database()

    def init_database(self):

        self.folder_path = Path(self.db_folder)
        self.db_path = Path(self.db_path)

        if not self.folder_path.exists():
            self.folder_path.mkdir(parents=True)

        if not self.db_path.exists():
            with open(self.db_path, "w"):
                pass

        self.connector()

        try:
            sql = f"SELECT name FROM sqlite_master WHERE type='type' and name='{self.table_name}'"
            self.cursor.execute(sql)
            result = self.cursor.fetchone()

            if result:
                return
            else:
                sql = f"""
                    CREATE TABLE '{self.table_name}' (
                    client_name	TEXT NOT NULL,
                    email	TEXT,
                    phone	NUMERIC,
                    address	TEXT,
                    contact	TEXT,
                    note	TEXT,
                    PRIMARY KEY("client_name")
                    );
                    """
                self.cursor.execute(sql)
                # Commit changes to the database
                self.connection.commit()

        except Exception as e:
            self.connection.rollback()
            return e

        finally:
            self.cursor.close()
            self.connection.close()

    def connector(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def common_search_execute(self, sql):
        self.connector()

        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except Exception:
            return None

        finally:
            self.cursor.close()
            self.connection.close()

    def get_data(self, search_flag="", client_name=""):

        if search_flag == "ALL":
            sql = (f"SELECT client_name, email, phone, address, contact, note FROM {self.table_name}")

        else:
            sql = (f"SELECT client_name, email, phone, address, contact, note FROM {self.table_name}"
                f"WHERE client_name='{client_name}'")

        result = self.common_search_execute(sql=sql)
        return result

    def get_all_clients(self):
        data = self.get_data(search_flag="ALL")

        return data

    def get_csv_file_path(self):

        csv_files = glob(join(self.csv_folder, "*.csv"))

        if csv_files:
            self.csv_path = Path(csv_files[0])

        else:
            error_message = "No CSV files found in the directory"
            print(error_message)
            raise FileNotFoundError(error_message)

    def insert_csv(self):

        df = pd.read_csv(self.csv_path, dtype=object)

        try:

            with sqlite3.connect(self.db_path) as conn:
                # Insert Dataframe into SQL Server:
                for index, row in df.iterrows():
                    cursor = conn.cursor()
                    cursor.execute(f"INSERT INTO {self.table_name} (client_name, email, phone, address, contact, note) values(?,?,?,?,?,?)",
                                (row.iloc[0],row.iloc[1],row.iloc[2],row.iloc[3],row.iloc[4],row.iloc[5]))

                conn.commit()

        except Exception as e:
            print(f"An error occurred while inserting CSV data: {e}")


# if __name__ == "__main__":

#     con = DataBaseConnect()
#     con.insert_csv()
