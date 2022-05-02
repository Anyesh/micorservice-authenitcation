import objectpath


class DataQuery:

    tree = None

    def __init__(self, json_data):
        self.tree = objectpath.Tree(json_data)

    def queryObjectTree(self, json_query):

        return list(self.tree.execute(json_query))

    def getObjectFilterString(self, argument_dictionary: dict):

        filter_string = ""
        if len(argument_dictionary.items()) > 0:
            filter_string = "["

            for i, (k, v) in enumerate(argument_dictionary.items(), start=1):
                if type(v) == str:
                    v = "'{v}'".format(v=v)

                filter_string = filter_string + "@.{k} is {v}".format(k=k, v=v)

                if i < len(argument_dictionary.items()):
                    filter_string = f"{filter_string} and "

            filter_string = f"{filter_string}]"

        return filter_string


class DataStorage:

    data = None
    dq = None

    def __init__(self):
        self.loadData()
        self.dq = DataQuery(json_data=self.data)

    def loadData(self):

        self.data = [
            {"id": 100, "first_name": "Han", "last_name": "Solo"},
            {"id": 101, "first_name": "Leia", "last_name": "Organa"},
            {"id": 102, "first_name": "Luke", "last_name": "Skywalker"},
        ]

    def getUser(self, **kwargs):
        filter_string = self.dq.getObjectFilterString(argument_dictionary=kwargs)

        json_query = "$.*{filters}".format(filters=filter_string)

        return self.dq.queryObjectTree(json_query=json_query)
