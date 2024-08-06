from data_preparation import load_and_prepare_data
from embedding_generation import generate_embeddings
from milvus_operations import connect_to_milvus, create_collection, insert_data, create_index, search_similar_records

def main():
    print("-"*140)
    # Carregar e preparar dados
    df = load_and_prepare_data("../PLN_2024_Soares_Pedro/data/rde-publicacao-12000.json")
    texts = df['combined_text'].tolist()

    print("[X] Load and prepare data\n")

    # Gerar embeddings
    embeddings, model = generate_embeddings(texts)

    print("[X] Generete embeddings\n")

    # Conectar-se ao Milvus
    connect_to_milvus()

    # Criar a coleção no Milvus
    collection_name = "DatasetCollection"
    embedding_dim = embeddings.shape[1]
    collection = create_collection(collection_name, embedding_dim)

    print("[X] Create collection Milvus\n")

    # Preparar dados para inserção
    data = [
        df['combined_text'].tolist(),
        embeddings.tolist()
    ]

    # Inserir dados na coleção
    insert_data(collection, data)

    print("[X] Insertion data in collection\n")

    # Criar o índice e carregar a coleção na memória
    create_index(collection)
    
    print("[X] All process completed")
    print("-"*140)
    
    # Perguntar ao usuário se ele quer digitar queries ou usar as predefinidas
    choice = input("Deseja digitar suas próprias queries? (s/n): ").strip().lower()

    if choice == 's':
        user_queries = []
        print("Digite suas queries (digite 'sair' para terminar):")
        while True:
            user_query = input("Query: ").strip()
            if user_query.lower() == 'sair':
                break
            user_queries.append(user_query)
        test_queries(user_queries, collection, model)
    else:
        # Queries de teste predefinidas
        default_queries = [
            "LIDER TAXI AEREO S/A - AIR BRASIL | LIDER INTL.AVIATION BV | PAISES BAIXOS (HOLAN | ARRENDAMENTO MERCANTIL | USD",
            "LIDER TAXI AEREO S/A - AIR BRASIL |  |  | ARRENDAMENTO MERCANTIL | BRL",
            " |  |  |  | EUR",
            " | Estrangeira | Brasil |  | USD",
            "BRASIL TELECOM | TELECOMUNICATIONS COMPANY | BRASIL | EXPORTAÇÃO | USD",
            "A TEC GRECO PROJS.E EQUIPS.LTDA | A TEC BETEILIGUNGSVERWALTUNGS GMBH | AUSTRIA | EUR"
        ]
        test_queries(default_queries, collection, model)

def test_queries(queries, collection, model):
    for query in queries:
        results = search_similar_records(
            query_text=query,
            collection=collection,
            model_name=model,
            top_k=3
        )

        # Exibir resultados da busca
        print(f"\nResultados da busca por similaridade semântica para a query: \n'{query}'")
        print("="*140)
        print(f"{'Similaridade':<15} {'Texto':<100}")
        print("="*140)

        for result in results[0]:
            similarity = round(result.distance, 4)
            text = result.entity.get('combined_text')
            print(f"{similarity:<15} {text:<100}")

        print("="*140)

if __name__ == "__main__":
    main()