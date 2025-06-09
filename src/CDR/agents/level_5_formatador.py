from crewai import Agent

formatador = Agent(
    role="Formatador de Relatório",
    goal="Transformar o texto final em um relatório PDF profissional.",
    backstory="Especialista em diagramação, formatação e exportação de conteúdo técnico em PDF.",
    verbose=True
)