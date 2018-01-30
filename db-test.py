import sqlite3
from util import post_listing_to_slack
from slackclient import SlackClient
import settings

sc = SlackClient(settings.SLACK_TOKEN)

con = sqlite3.connect('listings.db')

# with con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     # print("SQLite version: %s" % data)
#     cur.execute("SELECT * FROM Listings")
#     rows = cur.fetchone()
#     for row in rows:
#         print(row)
#
# post_listing_to_slack(sc, rows)

# deletes entire table !!!
# with con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE IF EXISTS Listings")
