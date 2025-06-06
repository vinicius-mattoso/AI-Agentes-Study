# from crewai import Task
# from agents.level_1_lider import lider
# from textwrap import dedent
# # mission_task = Task(
# #     description="Receber e estruturar os dados iniciais da empresa, objetivo do projeto e prazos.",
# #     expected_output="Estrutura inicial da missão com nome da empresa, tema, prazo e objetivo.",
# #     agent=lider,
# #     input={
# #         "conteudo": dedent("""
# #             Nome da Empresa: TechNova Solutions
# #             Tema do Projeto: Automatização de processos com IA
# #             Objetivo: Reduzir tempo de resposta ao cliente em 40%
# #             Prazo: 2 meses
# #             Contexto: Empresa do setor de logística, com foco em distribuição de última milha.
# #         """)
# #     }
# # )

# conteudo = dedent("""
#     Nome da Empresa: TechNova Solutions
#     Tema do Projeto: Automatização de processos com IA
#     Objetivo: Reduzir tempo de resposta ao cliente em 40%
#     Prazo: 12 meses
#     Contexto: Empresa do setor de logística, com foco em distribuição de última milha.
# """)

# mission_task = Task(
#     description=dedent(f"""
#         Com base nas informações abaixo, você deve estruturar os dados iniciais da empresa, objetivo do projeto e prazos. Para fornecer ao restante da equipe material para a criação de um relatório de CDR Critical Desing Review

#         {conteudo}
#     """),
#     expected_output="Estrutura inicial da missão com nome da empresa, tema, prazo e objetivo.",
#     agent=lider
# )

from crewai import Task
from agents.level_1_lider import lider
from textwrap import dedent
from datetime import datetime

# Pega mês e ano atual
data_hoje = datetime.now()
mes_ano = data_hoje.strftime("%B de %Y")  # exemplo: "June de 2025"

conteudo = dedent("""
    Nome da Empresa: Itau
    Tema do Projeto: Automatização de processos com IA
    Objetivo: Reduzir tempo de resposta ao cliente em 40%
    Prazo: 12 meses
    Contexto: Empresa do setor de bancário, que deseja reduzir o tempo de resposta a um cliente quando o mesmo tentar entrar em contato com o banco.
""")

mission_task = Task(
    description=dedent(f"""
        Você é o agente líder de um time de análise de projetos para inovação tecnológica.

        A data atual é {mes_ano}. Use isso para estimar a data de conclusão do projeto com base no prazo fornecido.

        Com base nas informações abaixo, extraia e estruture os dados essenciais para um relatório de CDR (Critical Design Review).

        As informações são:

        {conteudo}

        Sua resposta deve conter os seguintes campos formatados:
        - Nome da Empresa
        - Tema do Projeto
        - Objetivo
        - Prazo (incluir mês e ano de término estimado)
        - Contexto
    """),
    expected_output="Um resumo estruturado da missão com os campos bem definidos e prazo estimado de término.",
    agent=lider
)