# from crewai import Agent


# pesquisador = Agent(
#     role="Agente de Pesquisa",
#     goal="Pesquisar informações relevantes sobre a empresa, setor e soluções tecnológicas similares.",
#     backstory="Você é um pesquisador com acesso à web, especializado em contextualização de negócios e inovação tecnológica.",
#     verbose=True
# )

from crewai import Agent
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

web_rag_tool = WebsiteSearchTool()

pesquisador = Agent(
    role="Agente de Pesquisa",
    goal="Pesquisar informações relevantes sobre a empresa, setor e soluções tecnológicas similares.",
    backstory="Você é um pesquisador com acesso à web, especializado em contextualização de negócios e inovação tecnológica.",
    tools=[web_rag_tool],
    verbose=True
)