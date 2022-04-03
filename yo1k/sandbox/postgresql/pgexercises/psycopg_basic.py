import psycopg2
from psycopg2 import sql
# from psycopg2._psycopg import connection


def full_table_query(schema_name: str = "cd", table_name: str = "members") -> tuple:
    """Fetch a whole table from `exercises` database and return tuple of all records."""
    conn = psycopg2.connect(
            dbname="exercises",
            user="postgres",
            host="127.0.0.1")
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql.SQL("SELECT * FROM {0}.{1};").format(
                    sql.Identifier(schema_name),
                    sql.Identifier(table_name)))
            record: tuple = cur.fetchone()
    conn.close()
    return record


def top_revenue_query() -> tuple:
    """Finds the top three revenue generating facilities (question from `Aggregates` exercises).

    Produces a list of the top three revenue generating facilities (including ties). Output
    facility name and rank, sorted by rank and facility name.
     """
    conn = psycopg2.connect(
            dbname="exercises",
            user="postgres",
            host="127.0.0.1")
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                    """
                    SELECT
                        name,
                        rank
                    FROM (
                        SELECT
                            facs.name AS name,
                            rank() OVER (ORDER BY SUM(bks.slots * CASE
                                    WHEN bks.memid = 0 THEN facs.guestcost
                                    ELSE facs.membercost
                                END) DESC
                                ) AS rank
                        FROM
                            cd.bookings bks
                            INNER JOIN cd.facilities facs
                                ON bks.facid = facs.facid
                        GROUP BY
                            facs.name
                        ) as facs_rev
                    WHERE
                        rank <= 3  -- SKTODO prepared statement
                    ORDER BY
                        rank;
                    """)
            records = cur.fetchall()
    conn.close()
    return records


def record_types(rec):
    for i in rec:
        print(f"{i}: {type(i)}")


def show_table(records):
    for rec in records:
        print(rec)


if __name__ == "__main__":
    record_types(full_table_query(table_name="facilities"))
    show_table(top_revenue_query())
