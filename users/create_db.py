import sqlite3

con = sqlite3.connect("users.db")
cur = con.cursor()

cur.execute("""INSERT INTO users VALUES(
'rayformatics', '$6$qH69G49Vgeh11xxz$LMH04iWhgOogEVZAs/wR7bvC2a5lxpHItZXbb7aDIroGOD7WBXGtgJW8vorpR0rnVdWdkawaJqStMmpDB3k5C.', 'secureftp', 'rayformatics', '2225', 'n.hautevelle@viacesi.fr');""")

cur.execute("""INSERT INTO users VALUES(
'rayman','$6$q1SSTeH7iQ90UlAN$p.0Pvt.ciUdKY0wdaSYPkEqCujnYcWXP2vPRO2Dl8P8r1ANZ8LUdd4VZYdT6PqdKt93vSYf18OXRJ3gcHkvoZ.' ,'secureftp', 'discordbot', '2222', 'webmaster@rayformatics.fr');""")

cur.execute("""INSERT INTO users VALUES(
'kent','$6$nj.pKZXg3ChUppqc$UoKW86WrNpKL2vHHyvrYWuSj4jzhpiDRgPOlKam.8NyMsVqMJrTtp4H/XQSE8h36LFk3dEOAodyUmUsMX1HPk1', 'secureftp', 'kent', '2224', 'quentin.arrachart@viacesi.fr');""")

con.commit()

con.close()
