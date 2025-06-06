# from crewai import Task
# from agents.level_5_formatador import formatador
# from tasks.guardrail_tasks import revisar_task

# pdf_task = Task(
#     description="""
#         Você deve formatar o conteúdo validado de forma clara e profissional, pronto para ser convertido em um arquivo PDF.

#         ⚠️ Atenção:
#         - Remova qualquer pensamento, comentário interno, logs, ações ou instruções técnicas da inteligência artificial.
#         - Mantenha apenas o conteúdo útil e final, bem estruturado.
#         - Organize o conteúdo com:
#             - Capa com título e nome da empresa
#             - Sumário
#             - Seções como Introdução, Metodologia, Resultados, Conclusão
#             - Texto corrido com estilo corporativo e profissional
#         - Não inclua nenhuma marcação Markdown, código, ou formatação técnica.
#         - Escreva como se fosse um relatório executivo entregue para um diretor.

#         Use apenas o conteúdo validado da tarefa anterior como base.
#     """,
#     expected_output="Um conteúdo limpo, profissional e final para ser exportado como PDF corporativo.",
#     agent=formatador,
#     context=[revisar_task]
# )

from crewai import Task
from agents.level_5_formatador import formatador
from tasks.guardrail_tasks import revisar_task
from contexto.context_loader import carregar_contexto
from textwrap import dedent

ctx = carregar_contexto()
projeto = ctx['projeto']
publico = ctx['publico_alvo']

# Variáveis úteis
nome_empresa = projeto['empresa']
tema = projeto['objetivo']
setor = projeto['setor']
tom = publico['linguagem']
perfil = publico['perfil']

pdf_task = Task(
    description=dedent(f"""
        Formate o conteúdo validado do relatório para que fique pronto para exportação em PDF. O conteúdo deve ser convertido em um texto contínuo com estilo executivo, já estruturado em Markdown (extensão .md).

        Instruções:
        - ⚠️ Remova qualquer marcação interna de AI (ex: Thought, Action, Observations, etc.).
        - ❌ Não inclua comentários de raciocínio, logs de agente, instruções técnicas ou explicações sobre o próprio texto.
        - ✅ Utilize estrutura de relatório profissional com as seguintes partes:

        ---
        # Capa
        - Título do projeto
        - Nome da empresa ({nome_empresa})
        - Tema: {tema}
        - Setor: {setor}
        - Data de geração

        ---
        # Sumário
        - Listagem das seções e subtítulos

        ---
        # Introdução
        [Inserir texto validado da introdução]

        # Metodologia
        [Inserir texto validado da metodologia]

        # Conclusão
        [Inserir texto validado da conclusão]

        ---
        Requisitos:
        - O tom deve ser: {tom}
        - O texto deve ser adequado para: {perfil}
        - Sem jargões excessivos. Clareza e fluidez são essenciais.
        - O output deve estar completamente pronto para exportação como `.md`.

        Ao final, entregue apenas o conteúdo final já formatado.
    """),
    expected_output="Texto completo e formatado em estilo Markdown (.md), pronto para exportação em PDF.",
    agent=formatador,
    context=[revisar_task]
)
