import unittest
import subprocess
import tempfile
import os
from iranagent.cli import IranAgent
from .advanced_example import advanced
from .basic_example import main
from .auto_example import auto
# from xmlrunner import XMLTestRunner

# Patch for collections.abc MutableMapping issue
import collections.abc
collections.MutableMapping = collections.abc.MutableMapping

class TestIranAgentFramework(unittest.TestCase):
    def test_agents_advanced(self):
        iranagent = IranAgent(agent_file='tests/agents-advanced.yaml')
        result = iranagent.run()
        self.assertIsNotNone(result)

    def test_autogen_agents(self):
        iranagent = IranAgent(agent_file='tests/autogen-agents.yaml')
        result = iranagent.run()
        self.assertIsNotNone(result)

    def test_crewai_agents(self):
        iranagent = IranAgent(agent_file='tests/crewai-agents.yaml')
        result = iranagent.run()
        self.assertIsNotNone(result)

    def test_search_tool_agents(self):
        iranagent = IranAgent(agent_file='tests/search-tool-agents.yaml')
        result = iranagent.run()
        self.assertIsNotNone(result)

    def test_inbuilt_tool_agents(self):
        iranagent = IranAgent(agent_file='tests/inbuilt-tool-agents.yaml')
        result = iranagent.run()
        self.assertIsNotNone(result)

class TestIranAgentCommandLine(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)

    def test_iranagent_command(self):
        command = "iranagent --framework autogen --auto create movie script about cat in mars"
        result = subprocess.run(command.split(), capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)

    def test_iranagent_init_command(self):
        command = "iranagent --framework autogen --init create movie script about cat in mars"
        result = subprocess.run(command.split(), capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)

class TestExamples(unittest.TestCase):
    def test_basic_example(self):
        # Assuming main() has been adjusted to return a value for assertion
        result = main()
        self.assertIsNotNone(result)  # Adjust this assertion based on the expected outcome of main()

    def test_advanced_example(self):
        # Assuming advanced() returns a value suitable for assertion
        result = advanced()
        self.assertIsNotNone(result)  # Adjust this assertion as needed

    def test_auto_example(self):
        # Assuming auto() returns a value that can be asserted
        result = auto()
        self.assertIsNotNone(result)  # Adjust this assertion according to what auto() is expected to do

if __name__ == '__main__':
    # runner = XMLTestRunner(output='test-reports')
    unittest.main()
    # unittest.main(testRunner=runner, exit=False)