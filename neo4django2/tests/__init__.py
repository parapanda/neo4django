def setup():
    global neo4django2, neo4jrestclient, gdb, Person, settings, neo_constants

    from django.conf import settings

    import neo4django2, neo4jrestclient.client as neo4jrestclient
    from neo4django2.db import models
    from neo4django2.db import connection as gdb
    import neo4jrestclient.constants as neo_constants

    class Person(models.NodeModel):
        name = models.StringProperty()
        age = models.IntegerProperty(indexed=True)

def teardown():
    gdb.cleandb()
