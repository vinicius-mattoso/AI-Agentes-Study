from crewai import Task, Crew
from agents.level_2_pesquisador import pesquisador

# Task para testar o WebsiteSearchTool
task = Task(
    description=(
        "Pesquise informações atualizadas sobre a empresa Magazine Luiza, como setor de atuação, concorrência e tendências tecnológicas. "
        "Use seu conhecimento e acesso à internet para buscar em fontes confiáveis."
    ),
    agent=pesquisador,
    expected_output="Um resumo profissional com dados atuais da Magazine Luiza.",
)

# Monta e executa a crew com esse único agente e task
crew = Crew(
    agents=[pesquisador],
    tasks=[task],
    verbose=True
)

resultado = crew.kickoff()

print("\n📝 Resultado Final:\n")
print(resultado)
