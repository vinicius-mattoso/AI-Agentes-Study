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
    with open("relatorio_final.md", "w", encoding="utf-8") as f:
        f.write("--- RELATÓRIO FINAL ---")
        f.write(str(resultado))
    print("--- RELATÓRIO FINAL SALVO EM 'relatorio_final.md' ---")
    # Converter .md para .pdf
    try:
        import markdown
        import pdfkit

        with open("relatorio_final.md", "r", encoding="utf-8") as md_file:
            html_content = markdown.markdown(md_file.read())

        pdfkit.from_string(html_content, "relatorio_final.pdf")
        print("--- PDF gerado com sucesso: 'relatorio_final.pdf' ---")
    except Exception as e:
        print("Erro ao gerar PDF:", e)
