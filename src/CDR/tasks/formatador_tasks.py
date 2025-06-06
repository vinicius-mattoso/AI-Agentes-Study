from crewai import Task
from agents.level_5_formatador import formatador
from tasks.guardrail_tasks import revisar_task

pdf_task = Task(
    description="""
        Você deve formatar o conteúdo validado de forma clara e profissional, pronto para ser convertido em um arquivo PDF.

        ⚠️ Atenção:
        - Remova qualquer pensamento, comentário interno, logs, ações ou instruções técnicas da inteligência artificial.
        - Mantenha apenas o conteúdo útil e final, bem estruturado.
        - Organize o conteúdo com:
            - Capa com título e nome da empresa
            - Sumário
            - Seções como Introdução, Metodologia, Resultados, Conclusão
            - Texto corrido com estilo corporativo e profissional
        - Não inclua nenhuma marcação Markdown, código, ou formatação técnica.
        - Escreva como se fosse um relatório executivo entregue para um diretor.

        Use apenas o conteúdo validado da tarefa anterior como base.
    """,
    expected_output="Um conteúdo limpo, profissional e final para ser exportado como PDF corporativo.",
    agent=formatador,
    context=[revisar_task]
)