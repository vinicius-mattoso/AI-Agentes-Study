import yaml
import os

def carregar_contexto(path=None):
    if not path:
        path = os.path.join(os.path.dirname(__file__), 'contexto.yml')
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
