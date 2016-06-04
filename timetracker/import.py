import json
from db import r

data = json.loads(open("/home/traverseda/.ti-sheet-machina","r").read())

r.table('work').insert(data['work']).run()

data = json.loads(open("/home/traverseda/.ti-sheet","r").read())

r.table('work').insert(data['work']).run()

