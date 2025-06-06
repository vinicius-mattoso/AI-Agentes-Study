from crewai import Task
from agents.level_5_formatador import formatador
from tasks.guardrail_tasks import revisar_task

pdf_task = Task(
    description="Formatar o conteúdo validado e criar um PDF com capa, sumário e seções organizadas.",
    expected_output="PDF final do relatório formatado com estilo corporativo.",
    agent=formatador,
    context=[revisar_task]
)