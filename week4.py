import json
import sqlite3

filename = input("Enter the filename\n>> ")
if len(filename) <1:
	filename = 'roster_data.json'

try :
	with open(r'/home/froggy/Programs/Python/coursera/{0}'.format(filename)) as fp:
		raw_data = fp.read()
		json_data = json.loads(raw_data)

except(FileNotFoundError):
	print("Wrong file name. Re-Run the program.")
	exit()

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
	DROP TABLE IF EXISTS User;
	DROP TABLE IF EXISTS Member;
	DROP TABLE IF EXISTS Course;''')
cur.executescript('''
	CREATE TABLE User (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name UNIQUE);
	CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE);
	CREATE TABLE Member (user_id INTEGER, course_id INTEGER, role INTEGER, PRIMARY KEY (user_id, course_id));
	''')

for entry in json_data:
	name = entry[0]
	course = entry[1]
	role = entry[2]
	print((name, course, role))

	cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
	cur.execute('SELECT id FROM User WHERE NAME = ?', (name,))
	user_id = cur.fetchone()[0]

	cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course, ))
	cur.execute('SELECT id FROM Course WHERE title = ?', (course,))
	course_id = cur.fetchone()[0]

	cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)',(user_id, course_id, role))

	conn.commit()


