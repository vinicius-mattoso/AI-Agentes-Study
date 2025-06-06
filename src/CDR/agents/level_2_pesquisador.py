from crewai import Agent


pesquisador = Agent(
    role="Agente de Pesquisa",
    goal="Pesquisar informações relevantes sobre a empresa, setor e soluções tecnológicas similares.",
    backstory="Você é um pesquisador com acesso à web, especializado em contextualização de negócios e inovação tecnológica.",
    verbose=True
)