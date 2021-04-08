# Import Required modules
import json
import os
import sys
import random
import string
import argparse
import time
import commands
import colorama
import sqlite3
from colorama import Fore
from colorama import Style

# Do argument parser
parser = argparse.ArgumentParser()

# Open localdb
con = sqlite3.connect("/home/docker/users/users.db")
cur = con.cursor()

# Add arguments
parser.add_argument("-u", "--username", help="Specify username")
parser.add_argument("-em","--email", help="Specify email")
parser.add_argument("-i", "--image", help="Specify docker image")
parser.add_argument("-vol", "--volume", help="Specify name of volume")
parser.add_argument("-p", "--port", help="Specify port number")
parser.parse_args()

# Fetch argument values
args = parser.parse_args()

# check if arguments are None
if args.username is None:
   print('Please specify username using --username or -u')
   exit()

if args.email is None:
   print('Please specify email using --email or -em')
   exit()

if args.image is None:
   image = "secureftp"
else:
   image = args.image

if args.volume is None:
   volname = args.username
else:
   volname = args.volume

if args.port is None:
   cur.execute("SELECT MAX(port) FROM users")
   rows = cur.fetchall()

   for row in rows:
      portnb = int(row[0])+1
else:
   portnb = args.port

# Create random passwords
def gen_random_string(char_set, length):
   if not hasattr(gen_random_string, "rng"):
       gen_random_string.rng = random.SystemRandom()
   return ''.join([ gen_random_string.rng.choice(char_set) for _ in xrange(length) ])

password_charset = string.ascii_letters + string.digits

# make arguments variables
username=args.username
email=args.email

# encrypt password
password=gen_random_string(password_charset, 12)
pwdencrypted=commands.getstatusoutput("openssl passwd -6 {0}".format(password))

# Verify if volume exist
cur.execute("SELECT volume FROM users WHERE volume = '{0}'".format(volname))
rows = cur.fetchall()

if len(rows) > 0:
   print "Volume {0} already in use. Please specify other volume name using -vol or --volume".format(volname)
   exit()

# Verify if port already defined
cur.execute("SELECT port FROM users WHERE port = '{0}'".format(portnb))
rows = cur.fetchall()

if len(rows) > 0:
   print "Port {0} already in use. Please specify other port name using -p or --port".format(portnb)
   exit()

# Verify if username exist
cur.execute("SELECT username FROM users WHERE username = '{0}'".format(args.username))
rows = cur.fetchall()

if len(rows) > 0:
   print "Username {0} already in use. Please specify another username using -u or --username".format(args.username)
   exit()

# INSERT CLIENT IN DATABASE
cur.execute("INSERT INTO users VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(args.username, pwdencrypted[1], image, volname, portnb, args.email))

con.commit()
con.close()

# Prepare mail message with htm model
mail = open('/home/docker/mailmodel.htm', 'r').read()
mailformat = mail.format(username, portnb, username, password)

# Prepare mail send command
command = 'echo "{0}" | mail -s "[RFC] Your FTP is ready !" {1} --content-type=text/html -a From:"Rayformatics Industries"\<no-reply@rayformatics.fr\>'.format(mailformat, email)

# Start volume creation & start docker with chroot options

print (Fore.CYAN + Style.BRIGHT + "Creation of docker volume ..." + Style.RESET_ALL)
os.system("bash /home/docker/volumes_create {0}".format(username))

print (Fore.CYAN + Style.BRIGHT +"Grant privileges to container ..."+ Style.RESET_ALL)
os.system("chown -hR ubuntu:www-data /var/lib/docker/volumes/{0}/_data".format(username))
os.system("chmod 750 /var/lib/docker/volumes/{0}".format(username))
time.sleep(3)

print (Fore.CYAN + Style.BRIGHT +"First run of the container ..."+ Style.RESET_ALL)
os.system("python /home/docker/docker_start.py -u {0}".format(username))

# Send email with user's params
print (Fore.CYAN + Style.BRIGHT +"Sending email to client ..."+ Style.RESET_ALL)
os.system(command)

print password
