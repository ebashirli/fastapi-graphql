import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from schema import Query, Mutation

import collections
collections_abc = getattr(collections, 'abc', collections)

app = FastAPI()

app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))

@app.get('/')
def ping():
    return {'ping': 'pong'}
