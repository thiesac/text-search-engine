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
    results = []
    for data in instance._data:
        file_path = data["nome_do_arquivo"]
        with open(file_path, "r") as file:
            lines = file.readlines()
            occurrences = []
            for line_number, line in enumerate(lines, start=1):
                if word.lower() in line.lower():
                    occurrences.append(
                        {"linha": line_number, "conteudo": line.strip()}
                    )
            if occurrences:
                result = {
                    "palavra": word,
                    "arquivo": file_path,
                    "ocorrencias": occurrences,
                }
                results.append(result)
    return results
