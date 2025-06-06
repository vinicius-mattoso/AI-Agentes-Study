from crewai import Task
from agents.level_4_guardrail import guardrail
from tasks.edicao_tasks import intro_task, metodo_task, conclusao_task

revisar_task = Task(
    description="Revisar todos os textos (introdução, metodologia e conclusão), corrigindo falhas gramaticais e possíveis erros éticos.",
    expected_output="Texto revisado e validado.",
    agent=guardrail,
    context=[intro_task, metodo_task, conclusao_task]
)
