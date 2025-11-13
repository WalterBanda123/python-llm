from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.lite_llm import LiteLlm;

root_agent = LlmAgent(
    model=LiteLlm(model='openai/gpt-4o-mini'),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
