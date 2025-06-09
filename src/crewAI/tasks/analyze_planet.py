from crewai import Task
from agents.scientist import scientist

analyze_planet_task = Task(
    description=(
        "Você deve realizar uma análise científica do planeta Estrela Azul, coletando dados sobre a atmosfera, solo, fauna e possíveis formas de vida."
    ),
    expected_output=(
        "Um relatório com dados e conclusões sobre as características científicas do planeta."
    ),
    agent=scientist
)
