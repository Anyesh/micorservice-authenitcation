from dataclasses import dataclass

from ariadne import QueryType, snake_case_fallback_resolvers
from ariadne_extensions.federation import FederatedManager, FederatedObjectType
from schema.data_interface import DataStorage


@dataclass
class BoundaryGeneric:
    def __init__(self, child_name, kwargs=None):
        self.typename = child_name

        if kwargs:
            self.update_class(kwargs)

        self.get_updated()

    def update_class(self, kwargs):
        for k, v in kwargs.items():
            if not hasattr(self, k):
                setattr(self, k, v)

    def get_updated(self):
        return self


@dataclass
class User(BoundaryGeneric):
    def __init__(self, **kwargs):
        super().__init__(self.__class__.__name__, kwargs)


class SchemaCreator:

    query = QueryType()
    user = FederatedObjectType("User")
    photo = FederatedObjectType("Photo")

    def __init__(self):
        self.ds = DataStorage()

    def getSchema(self):

        manager = FederatedManager(
            schema_sdl_file="schema/schema.graphql",
            query=self.query,
        )

        @self.query.field("posts")
        def resolve_posts(*_, **kwargs):
            return self.ds.getPost(**kwargs)

        @self.user.resolve_reference
        def resolve_user(representation):
            user_id = representation.get("id")
            return User(id=user_id)

        @self.user.field("photos")
        def resolve_user_photos(obj, info):
            kwargs = {"user_id": obj.id}

            return self.ds.getPhoto(**kwargs)

        manager.add_types(self.user, self.photo)
        manager.add_types(snake_case_fallback_resolvers)

        return manager.get_schema()
