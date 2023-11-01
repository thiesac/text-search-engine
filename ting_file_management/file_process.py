from file_management import txt_importer


def process(path_file, instance):
    """Processa o arquivo e o adiciona à fila, se ainda não estiver presente"""
    if path_file in [item["nome_do_arquivo"] for item in instance.items]:
        print(f"Arquivo {path_file} já processado, ignorando.")
    else:
        data = txt_importer(path_file)
        instance.enqueue(
            {"nome_do_arquivo": path_file, "linhas_do_arquivo": data}
        )
        print(
            f'{{\n "nome_do_arquivo": "{path_file}",\n'
            f'    "qtd_linhas": {len(data)},\n'
            f'    "linhas_do_arquivo": {data}\n}}'
        )


def remove(instance):
    """Remove o primeiro elemento da fila"""
    try:
        removed_item = instance.dequeue()
        print(
            f"Arquivo {removed_item['nome_do_arquivo']} removido com sucesso."
        )
    except IndexError:
        print("Não há elementos na fila, não é possível remover.")


def file_metadata(instance, position):
    """Obtém metadados do arquivo na posição especificada na fila"""
    try:
        file_data = instance.search(position)
        metadata = {
            "nome_do_arquivo": file_data["nome_do_arquivo"],
            "qtd_linhas": len(file_data["linhas_do_arquivo"]),
            "linhas_do_arquivo": file_data["linhas_do_arquivo"],
        }
        return metadata
    except IndexError:
        raise IndexError("Posição inválida na fila")
