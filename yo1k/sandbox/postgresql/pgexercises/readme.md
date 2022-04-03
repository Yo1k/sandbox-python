Contains some solutions to programming exercises 
from [pgexercises.com](https://www.pgexercises.com)
using [Psycopg](https://www.psycopg.org/docs/index.html) database adapter for the Python.

It includes `clubdata.sql` script for creating the database used in the exercises.
To create the database using a shell capable of running [Bash](https://www.gnu.org/software/bash/) 
scripts,
run the following from the directory with `clubdata.sql`:

```shell
$ psql -U postgres -f clubdata.sql -d postgres -x -q
```
