import json

import cohere

Cohere_API_KEY = "KvNeCIxL894TVk0gHXmbgjRyaHGYtAtwdBEwcx93"
co = cohere.Client(Cohere_API_KEY)


def generate_log_embeddings(log_file_path):
    """
    Generates embeddings for each logline in logfile in form of:
    {"embeddings": [
        {"log_line": "log line 1", "embedding": [0.1, 0.2, 0.3, ...], "id": 0},
    ]}
    Args:
        log_file_path: path to the log_file.out

    Returns:

    """
    with open(log_file_path, 'r', encoding='utf-8') as file:
        logs = file.readlines()
    needed_logs = logs
    embeds = co.embed(texts=needed_logs, model='embed-english-v3.0', input_type='search_document').embeddings
    results = {'embeddings': []}
    for i, embed in enumerate(embeds):
        results['embeddings'].append({'log_line': logs[i], 'embedding': embed, 'id': i})

    # Save the results to a json file
    with open('log_embeddings.json', 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    return embeds


def generate_query_embeddings(query):
    """
    Generates embeddings for a text query to be used for similarity search.

    Args:
        query [str]: query to be embedded

    Returns:
        embeds [list]: list of embeddings for the query

    """
    embeds = co.embed(texts=[query], model='embed-english-v3.0', input_type='search_query').embeddings
    return embeds[0]


if __name__ == '__main__':
    path_to_logs = r"C:\Users\Mohammad.Al-zoubi\Documents\projects\Querius\backend\QA\test_log_1k.out"
    query = "What are the error messages in this log?"

    # generate_log_embeddings(path_to_logs)
    generate_query_embeddings(query)