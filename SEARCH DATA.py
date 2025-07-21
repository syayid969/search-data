import sqlite3

koneksi_ke_DB = sqlite3.connect("vendingmachine.db")

k = koneksi_ke_DB.cursor()

k.execute("""
          SELECT * FROM TBvendingmachine
          WHERE
          id = 101
          """)
print(k.fetchall())

koneksi_ke_DB.close()