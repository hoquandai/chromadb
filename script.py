import chromadb

client = chromadb.HttpClient(host="chromadb", port=8000)
collection = client.get_or_create_collection("sample_collection")
# Add docs to the collection. Can also update and delete. Row-based API coming soon!
collection.add(
    documents=["This is document1", "This is document2"], # we embed for you, or bring your own
    metadatas=[{"source": "notion"}, {"source": "google-docs"}], # filter on arbitrary metadata!
    ids=["doc1", "doc2"], # must be unique for each doc
)
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2,
    # where={"metadata_field": "{'source': 'notion'}"}, # optional filter
    # where_document={"$contains":"search_string"}  # optional filter
)
