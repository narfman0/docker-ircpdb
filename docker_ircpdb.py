import ircpdb
import logging


logging.basicConfig(filename='debug.log', level=logging.DEBUG)


ircpdb.set_trace(
    channel="#bots",
    nickname='ircpdb_bot',
    #password='',
    server='localhost',
    limit_access_to=['narfman0', ],
    port=6667,
    #ssl=True,
)
