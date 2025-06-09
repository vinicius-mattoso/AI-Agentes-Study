import os
from dotenv import load_dotenv
from crewai import Crew

from agents.commander import commander
from tasks.mission_plan import mission_task

from agents.commander import commander
from agents.scientist import scientist
from agents.fieldbot import fieldbot
from agents.techwriter import techwriter
from tasks.mission_plan import mission_task
from tasks.write_report_task import write_report_task
from tasks.analyze_planet import analyze_planet_task
# Carregar a chave da API
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# # Criar a Crew
# crew = Crew(
#     agents=[commander],
#     tasks=[mission_task],
#     verbose=True
# )

crew = Crew(
    agents=[commander, scientist, techwriter],
    tasks=[mission_task,analyze_planet_task, write_report_task],
    verbose=True
)

# Rodar a missão
result = crew.kickoff()
print("\n\n--- PLANO DE MISSÃO ---\n")
print(result)
