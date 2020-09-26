import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
# print(conn)
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input("Enter file Name\n>> ")

if (len(fname) < 1):
	fname = 'mbox-short.txt'

fh = open(fname)

for line in fh:
	if not line.startswith('From: '):
		continue

	pieces = line.split()
	# print(pieces)
	email = pieces[1]
	org = email.split('@')[1]
	cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
	row = cur.fetchone()
	if row is None:
		cur.execute('INSERT INTO Counts (org, count) VALUES (?,  1)', (org, ))
	else:
		cur.execute('UPDATE Counts set count = count + 1 WHERE org = ?',(org, ))

	conn.commit()

#https://www.sqlite.org/lang_select.htmlsqlite3.OperationalError: database is locked

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
# print(type(sqlstr))

for row in cur.execute(sqlstr):
	print(str(row[0]), row[1])
cur.close()
