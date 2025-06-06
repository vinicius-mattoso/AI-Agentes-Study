from spire.doc import *
from spire.doc.common import *
import os


# Defina os caminhos de entrada e saída
input_md = "relatorio_final.md"
output_pdf = "relatorio_final.pdf"

# Verifica se o arquivo Markdown existe
if not os.path.exists(input_md):
    print(f"Arquivo '{input_md}' não encontrado.")
    exit(1)

# Cria o documento
document = Document()

try:
    # Carrega o arquivo Markdown
    document.LoadFromFile(input_md)

    # Salva como PDF
    document.SaveToFile(output_pdf, FileFormat.PDF)
    print(f"PDF gerado com sucesso: '{output_pdf}'")

except Exception as e:
    print("Erro ao converter Markdown para PDF:", e)

finally:
    # Libera os recursos
    document.Dispose()
