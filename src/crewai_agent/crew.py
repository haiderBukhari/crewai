from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CrewaiAgent:
    """CrewaiAgent crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def req_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['req_analyzer'],
            verbose=True
        )

    @agent
    def design_craft(self) -> Agent:
        return Agent(
            config=self.agents_config['design_craft'],
            verbose=True
        )

    @agent
    def code_mate(self) -> Agent:
        return Agent(
            config=self.agents_config['code_mate'],
            verbose=True
        )

    @agent
    def test_genie(self) -> Agent:
        return Agent(
            config=self.agents_config['test_genie'],
            verbose=True
        )

    @agent
    def deploy_wizard(self) -> Agent:
        return Agent(
            config=self.agents_config['deploy_wizard'],
            verbose=True
        )

    @agent
    def maintainer_ai(self) -> Agent:
        return Agent(
            config=self.agents_config['maintainer_ai'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_task'],
        )

    @task
    def development_task(self) -> Task:
        return Task(
            config=self.tasks_config['development_task'],
        )

    @task
    def testing_task(self) -> Task:
        return Task(
            config=self.tasks_config['testing_task'],
        )

    @task
    def deployment_task(self) -> Task:
        return Task(
            config=self.tasks_config['deployment_task'],
        )

    @task
    def maintenance_task(self) -> Task:
        return Task(
            config=self.tasks_config['maintenance_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiAgent crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
