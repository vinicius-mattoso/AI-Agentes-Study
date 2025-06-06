from crewai import Task
from agents.level_2_pesquisador import pesquisador
from tasks.lider_tasks import mission_task

pesquisa_task = Task(
    description="Pesquisar com base nas instruções do Líder: contexto da empresa, setor de atuação, tecnologias úteis.",
    expected_output="Resumo com informações da empresa, setor, tecnologias e benchmarks.",
    agent=pesquisador,
    context=[mission_task]
)