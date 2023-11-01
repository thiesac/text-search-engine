def process(path_file, instance):
    """Processa o arquivo e o adiciona à fila, se ainda não estiver presente"""
    if path_file in [item["nome_do_arquivo"] for item in instance._data]:
        return
    else:
        with open(path_file, "r") as file:
            data = [line.strip() for line in file]
            instance.enqueue(
                {"nome_do_arquivo": path_file, "linhas_do_arquivo": data}
            )


def remove(instance):
    """Remove o primeiro elemento da fila"""
    removed_item = instance.dequeue()
    if removed_item:
        print(
            f"Arquivo {removed_item['nome_do_arquivo']} removido com sucesso."
        )
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    """Obtém metadados do arquivo na posição especificada na fila"""
    file_data = instance.search(position)
    metadata = {
        "nome_do_arquivo": file_data["nome_do_arquivo"],
        "qtd_linhas": len(file_data["linhas_do_arquivo"]),
        "linhas_do_arquivo": file_data["linhas_do_arquivo"],
    }
    return metadata
