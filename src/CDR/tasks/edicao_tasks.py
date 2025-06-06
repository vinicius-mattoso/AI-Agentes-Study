from crewai import Task
from agents.level_3_editores import editor_intro, editor_metodo, editor_conclusao
from tasks.pesquisa_tasks import pesquisa_task

intro_task = Task(
    description="Criar a introdução do relatório com base nos dados da pesquisa.",
    expected_output="Texto de introdução com contextualização do problema.",
    agent=editor_intro,
    context=[pesquisa_task]
)

metodo_task = Task(
    description="Descrever a metodologia para resolver o problema da empresa.",
    expected_output="Texto explicando as etapas da abordagem e ferramentas utilizadas.",
    agent=editor_metodo,
    context=[pesquisa_task]
)

conclusao_task = Task(
    description="Redigir a conclusão do relatório, destacando os principais pontos e próximos passos.",
    expected_output="Texto de conclusão claro e objetivo.",
    agent=editor_conclusao,
    context=[intro_task, metodo_task]
)