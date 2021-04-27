import json
import os
import sqlite3
import subprocess
import argparse


# Do argument parser
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument("-u", "--username", help="Specify username")
parser.parse_args()

# Fetch argument values
args = parser.parse_args()

if args.username is not None:
   user = args.username
else:
   user = 0

# Open LocalDB
con = sqlite3.connect("/home/docker/users/users.db")
cur = con.cursor()

# Get all datas
if user is 0:
   cur.execute("SELECT * FROM users")
else:
    cur.execute("SELECT * FROM users WHERE username='{0}'".format(user))

rows = cur.fetchall()

for row in rows:
    username = row[0]
    password = row[1]
    image = row[2]
    volume = row[3]
    port = row[4]
    email = row[5]

    # Check if container already started
    try:
        inuse = subprocess.check_output("docker ps --filter 'name={0}' | grep '{0}'".format(username), shell=True)
        print "{0}'s container already started !".format(username)
    except subprocess.CalledProcessError as e:
        # Launch all containers
        os.system("bash /home/docker/volumes_create {0}".format(volume))
        os.system("chown -hR ubuntu:www-data /var/lib/docker/volumes/{0}".format(volume))
        os.system("chmod -R 770 /var/lib/docker/volumes/{0}".format(volume))
        os.system("docker run -p {2}:22 -e SSH_USER={0} -e SSH_PASSWORD='{1}' -v {3}:/home/public/public_html --link=sqlserver --name={0} -d {4}".format(username, password, port, volume, image))
        os.system("bash /home/docker/chroot_config {0}".format(username))
