import sys
import os


def txt_importer(path_file):
    if not os.path.isfile(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    elif not path_file.endswith("txt"):
        print("Formato inválido", file=sys.stderr)
    else:
        with open(path_file, "r") as file:
            content = file.read()
            piece_of_news = content.split("\n")
            return piece_of_news
