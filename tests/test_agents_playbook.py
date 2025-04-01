# tests/test_agents_playbook.py
import unittest
from iranagent import IranAgent

class TestIranAgentFramework(unittest.TestCase):
    def test_agents_playbook(self):
        iranagent = IranAgent(agent_file='tests/autogen-agents.yaml')
        result = iranagent.run()
        self.assertIsNotNone(result)

    def test_crewai_agents_playbook(self):
        iranagent = IranAgent(agent_file='tests/crewai-agents.yaml')
        result = iranagent.run()
        self.assertIsNotNone(result)

    def test_search_tool_agents_playbook(self):
        iranagent = IranAgent(agent_file='tests/search-tool-agents.yaml')
        result = iranagent.run()
        self.assertIsNotNone(result)

    def test_inbuilt_tool_agents_playbook(self):
        iranagent = IranAgent(agent_file='tests/inbuilt-tool-agents.yaml')
        result = iranagent.run()
        self.assertIsNotNone(result)