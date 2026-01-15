from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client

def perform_search(query, index_name='djapp_Product', **kwargs):
    client = get_client()
    # Direct search on the client
    results = client.search_single_index(
        index_name=index_name,
        search_params={'query': query, **kwargs}
    )
    return results

# def get_index(index_name='djapp_Product'):
#     client = get_client()
#     # print("Client",dir(client))
#     index = client.init_index(index_name)
#     return index

# def perform_search(query, **kwargs):
#     index = get_index()
#     params = {}
#     tags = ""
#     if "tags" in kwargs:
#         tags = kwargs.pop("tags") or []
#         if len(tags) != 0:
#             params['tagFilter'] = tags
#     results = index.search(query, **kwargs)
#     return results






