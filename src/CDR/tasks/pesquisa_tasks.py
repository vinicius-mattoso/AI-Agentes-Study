# from crewai import Task
# from agents.level_2_pesquisador import pesquisador
# from tasks.lider_tasks import mission_task

# pesquisa_task = Task(
#     description="Pesquisar com base nas instruções do Líder: contexto da empresa, setor de atuação, tecnologias úteis.",
#     expected_output="Resumo com informações da empresa, setor, tecnologias e benchmarks.",
#     agent=pesquisador,
#     context=[mission_task]
# )

from crewai import Task
from agents.level_2_pesquisador import pesquisador
from tasks.lider_tasks import mission_task
from contexto.context_loader import carregar_contexto
from textwrap import dedent

ctx = carregar_contexto()
projeto = ctx['projeto']
pesquisa_cfg = ctx['agentes']['pesquisador']

pesquisa_task = Task(
    description=dedent(f"""
        Com base nas instruções da liderança e nos dados do projeto, realize uma pesquisa aprofundada e direcionada.

        A empresa em foco é: {projeto['empresa']}
        Setor: {projeto['setor']}
        Objetivo do projeto: {projeto['objetivo']}

        Pontos de pesquisa prioritários:
        - {pesquisa_cfg['pontos_focais'][0]}
        - {pesquisa_cfg['pontos_focais'][1]}
        - {pesquisa_cfg['pontos_focais'][2]}

        Tipo de fonte recomendada: {pesquisa_cfg['tipo_de_fonte']}

        Estruture a resposta com:
        - Visão geral do setor
        - Problemas comuns enfrentados
        - Tecnologias e soluções utilizadas por concorrentes ou benchmarks
        - Informações úteis para ajudar os editores a redigir a metodologia e contextualização
    """),
    expected_output="Resumo com informações sobre setor, tecnologias utilizadas, concorrentes e práticas recomendadas.",
    agent=pesquisador,
    context=[mission_task]
)
