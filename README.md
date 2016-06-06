This is a collection of generic tools for interacting with rethinkdb.

Right now there's

 - rq

A generic text editor wrapper. It lets you edit rethinkdb paths like
"timetracker.work" to access your worklog.

You can also query based on indexes, so "rq timetracker.work.name:workedOnTi"
would get you all the database entries where the secondary key "name" equaled
"workedOnTi".

There's also a time tracker called

 - ti

A fork of [ti.sharats.me](http://ti.sharats.me/) that uses rethinkdb as it's backend. "rq" is partially
inspired by it's "ti e" command.

---

Add bin to your path.

Add this repo to your pythonpath.
