from collections.abc import Sequence, MutableSequence
from typing import Any
import psycopg2  # type: ignore
from psycopg2 import sql


def get_full_table(*table_name_parts: str) -> MutableSequence[Sequence[Any]]:
    """Fetch a whole table from `exercises` database and return tuple of all records."""
    conn = psycopg2.connect(
            dbname="exercises",
            user="postgres",
            host="127.0.0.1")
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql.SQL("SELECT * FROM {0};").format(
                    sql.Identifier(*table_name_parts)))
            records: MutableSequence[Sequence[Any]] = cur.fetchall()
    conn.close()
    return records


def top_revenue_query(rank: int = 3) -> MutableSequence[Sequence[Any]]:
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
                        rank <= %(rank)s
                    ORDER BY
                        rank;
                    """,
                    {"rank": rank}
            )
            records: MutableSequence[Sequence[Any]] = cur.fetchall()
    conn.close()
    return records


def print_value_type(records: MutableSequence[Sequence[Any]]) -> None:
    for i in records[0]:
        print(f"{i}: {type(i)}")


def print_table(records: MutableSequence[Sequence[Any]]) -> None:
    for rec in records:
        print(rec)


if __name__ == "__main__":
    print_value_type(get_full_table("cd", "facilities"))
    print_table(top_revenue_query())
