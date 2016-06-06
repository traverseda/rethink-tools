import rethinkdb as r
r.connect(db="timetracker").repl()

currentTables=r.table_list().run()
tables=['work','projects']

for table in tables:
    if table not in currentTables:
        r.table_create(table).run()

r=r
