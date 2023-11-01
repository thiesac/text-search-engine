def exists_word(word, instance):
    occurrences = []
    for file_data in instance._data:
        file_name = file_data["nome_do_arquivo"]
        lines_with_word = []
        for i, line in enumerate(file_data["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                lines_with_word.append({"linha": i})
        if lines_with_word:
            occurrences.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": lines_with_word,
                }
            )
    return occurrences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
