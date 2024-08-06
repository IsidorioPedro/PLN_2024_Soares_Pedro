from sentence_transformers import SentenceTransformer

# Função para gerar embeddings
def generate_embeddings(texts, model_name='intfloat/multilingual-e5-base'):
    model = SentenceTransformer(model_name)
    return model.encode(texts, convert_to_tensor=True), model
