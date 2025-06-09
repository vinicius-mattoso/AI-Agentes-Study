from crewai import Crew
from agents.level_1_lider import lider
from agents.level_2_pesquisador import pesquisador
from agents.level_3_editores import editor_intro, editor_metodo, editor_conclusao
from agents.level_4_guardrail import guardrail
from agents.level_5_formatador import formatador

from tasks.lider_tasks import mission_task
from tasks.pesquisa_tasks import pesquisa_task
from tasks.edicao_tasks import intro_task, metodo_task, conclusao_task
from tasks.guardrail_tasks import revisar_task
from tasks.formatador_tasks import pdf_task

from datetime import datetime

crew = Crew(
    agents=[
        lider, pesquisador,
        editor_intro, editor_metodo, editor_conclusao,
        guardrail, formatador
    ],
    tasks=[
        mission_task,
        pesquisa_task,
        intro_task, metodo_task, conclusao_task,
        revisar_task, pdf_task
    ],
    verbose=False
)

if __name__ == "__main__":
    resultado = crew.kickoff()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    md_path = f"relatorio_final_{timestamp}.md"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("--- RELATÓRIO FINAL ---\n\n")
        f.write(str(pdf_task.output))

    print(f"✅ Relatório salvo em: {md_path}")
