from crewai import Agent

editor_intro = Agent(
    role="Editor de Introdução",
    goal="Criar uma introdução sólida com base na pesquisa.",
    backstory="Especialista em escrita técnica e contextualização de problemas.",
    verbose=True
)

editor_metodo = Agent(
    role="Editor de Metodologia",
    goal="Definir claramente os métodos a serem utilizados na resolução do problema.",
    backstory="Especialista em engenharia de processos e planejamento estratégico.",
    verbose=True
)

editor_conclusao = Agent(
    role="Editor de Conclusão",
    goal="Apresentar uma conclusão objetiva e assertiva.",
    backstory="Redator técnico experiente em sínteses de projetos e relatórios.",
    verbose=True
)