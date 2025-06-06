from crewai import Task
from agents.level_1_lider import lider
from textwrap import dedent
# mission_task = Task(
#     description="Receber e estruturar os dados iniciais da empresa, objetivo do projeto e prazos.",
#     expected_output="Estrutura inicial da missão com nome da empresa, tema, prazo e objetivo.",
#     agent=lider,
#     input={
#         "conteudo": dedent("""
#             Nome da Empresa: TechNova Solutions
#             Tema do Projeto: Automatização de processos com IA
#             Objetivo: Reduzir tempo de resposta ao cliente em 40%
#             Prazo: 2 meses
#             Contexto: Empresa do setor de logística, com foco em distribuição de última milha.
#         """)
#     }
# )

conteudo = dedent("""
    Nome da Empresa: TechNova Solutions
    Tema do Projeto: Automatização de processos com IA
    Objetivo: Reduzir tempo de resposta ao cliente em 40%
    Prazo: 12 meses
    Contexto: Empresa do setor de logística, com foco em distribuição de última milha.
""")

mission_task = Task(
    description=dedent(f"""
        Com base nas informações abaixo, você deve estruturar os dados iniciais da empresa, objetivo do projeto e prazos. Para fornecer ao restante da equipe material para a criação de um relatório de CDR Critical Desing Review

        {conteudo}
    """),
    expected_output="Estrutura inicial da missão com nome da empresa, tema, prazo e objetivo.",
    agent=lider
)