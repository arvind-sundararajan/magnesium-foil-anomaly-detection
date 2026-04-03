```json
{
    "agents/tool_calling_agent.py": {
        "content": "
import logging
from typing import Dict, List
from relay.app import RelayApp
from openllm import OpenLLM
from phoenix import Phoenix

class ToolCallingAgent:
    """
    Agent responsible for calling tools and managing their output.
    """

    def __init__(self, config: Dict):
        """
        Initialize the agent with a configuration dictionary.

        Args:
        - config (Dict): Configuration dictionary containing tool settings.
        """
        self.config = config
        self.relay_app = RelayApp()
        self.openllm = OpenLLM()
        self.phoenix = Phoenix()
        self.logger = logging.getLogger(__name__)

    def call_tool(self, tool_name: str, params: Dict) -> Dict:
        """
        Call a tool with the given parameters.

        Args:
        - tool_name (str): Name of the tool to call.
        - params (Dict): Parameters to pass to the tool.

        Returns:
        - Dict: Output of the tool call.
        """
        try:
            self.logger.info(f'Calling tool {tool_name} with params {params}')
            output = self.relay_app.call_tool(tool_name, params)
            self.logger.info(f'Tool {tool_name} output: {output}')
            return output
        except Exception as e:
            self.logger.error(f'Error calling tool {tool_name}: {e}')
            raise

    def manage_output(self, output: Dict) -> None:
        """
        Manage the output of a tool call.

        Args:
        - output (Dict): Output of the tool call.
        """
        try:
            self.logger.info(f'Managing output: {output}')
            non_stationary_drift_index = self.openllm.calculate_non_stationary_drift_index(output)
            stochastic_regime_switch = self.phoenix.detect_stochastic_regime_switch(output)
            self.logger.info(f'Non-stationary drift index: {non_stationary_drift_index}')
            self.logger.info(f'Stochastic regime switch: {stochastic_regime_switch}')
        except Exception as e:
            self.logger.error(f'Error managing output: {e}')
            raise

    def simulate_rocket_science(self) -> None:
        """
        Simulate the 'Rocket Science' problem.
        """
        try:
            self.logger.info('Simulating Rocket Science problem')
            tool_name = 'rocket_science_tool'
            params = {'fuel': 100, 'velocity': 200}
            output = self.call_tool(tool_name, params)
            self.manage_output(output)
        except Exception as e:
            self.logger.error(f'Error simulating Rocket Science problem: {e}')
            raise

if __name__ == '__main__':
    config = {'tool_settings': {'rocket_science_tool': {'fuel': 100, 'velocity': 200}}}
    agent = ToolCallingAgent(config)
    agent.simulate_rocket_science()
",
        "commit_message": "feat: implement specialized tool_calling_agent logic"
    }
}
```