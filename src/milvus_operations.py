from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility

def connect_to_milvus(host="localhost", port="19530"):
    connections.connect("default", host=host, port=port)

def create_collection(collection_name, embedding_dim):
    # Se a coleção já existir, exclua-a
    if utility.has_collection(collection_name):
        collection = Collection(collection_name)
        collection.drop()
        #print(f"Coleção '{collection_name}' excluída com sucesso.")

    # Definir o esquema da coleção
    fields = [
        FieldSchema(name="record_id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="combined_text", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=embedding_dim)
    ]
    schema = CollectionSchema(fields, "Informações do dataset")

    # Criar a coleção
    collection = Collection(collection_name, schema)
    return collection

def insert_data(collection, data):
    # Inserir dados na coleção
    collection.insert(data)

def create_index(collection):
    # Criar um índice para os embeddings
    index_params = {
        "metric_type": "L2",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128}
    }
    collection.create_index("embeddings", index_params)
    collection.load()

def search_similar_records(query_text, collection, model_name='intfloat/multilingual-e5-base',top_k=5):
    # Gerar embeddings para o texto de consulta
    query_embedding = model_name.encode([query_text], convert_to_tensor=True)
    
    # Executar a consulta no Milvus
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    results = collection.search(
        data=query_embedding.tolist(),
        anns_field="embeddings",
        param=search_params,
        limit=top_k,
        expr=None,
        output_fields=["record_id", "combined_text"]
    )
    
    return results

