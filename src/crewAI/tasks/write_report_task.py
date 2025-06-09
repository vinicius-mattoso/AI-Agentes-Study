from crewai import Task
from agents.techwriter import techwriter

write_report_task = Task(
    description=(
        "Você deve compilar os resultados da missão, incluindo análises científicas, decisões táticas e dados de campo, "
        "em um relatório técnico claro, conciso e detalhado para a Frota Intergaláctica. "
        "Certifique-se de que o relatório seja compreensível até mesmo por membros não técnicos da frota."
    ),
    expected_output=(
        "Um relatório técnico completo com seções bem definidas, como Introdução, Metodologia, Descobertas, Análises e Conclusão."
    ),
    agent=techwriter
)
