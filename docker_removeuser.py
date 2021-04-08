import json
import os
import sys
import sqlite3

if not sys.argv[1:]:
   print "Please specify the container name"
   exit()

username = sys.argv[1]

# Kill container
os.system("docker kill {0}".format(username))
os.system("docker rm {0}".format(username))

# Open LocalDB
con = sqlite3.connect("/home/docker/users/users.db")
cur = con.cursor()

# Delete associated volume & Remove line in localdb
cur.execute("SELECT volume FROM users WHERE username='{0}'".format(username))
rows = cur.fetchall()

for row in rows:
    # Remove associated volume
    os.system("bash /home/docker/volumes_remove {0}".format(row[0]))

cur.execute("DELETE FROM users WHERE username='{0}'".format(username))
con.commit()
con.close()
