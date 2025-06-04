from crewai import Task
from agents.commander import commander

mission_task = Task(
    description='Planejar toda a missão de exploração do planeta Estrela Azul, definindo etapas, riscos e prioridades.',
    expected_output='Um plano detalhado com as fases da missão e os responsáveis por cada tarefa.',
    agent=commander
)
