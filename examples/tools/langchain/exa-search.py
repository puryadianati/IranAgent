from praisonaiagents import Agent, PraisonAIAgents
from exa_py import Exa
import os

exa = Exa(api_key=os.environ["EXA_API_KEY"])

def search_and_contents(query: str):
    """Search for webpages based on the query and retrieve their contents."""
    # This combines two API endpoints: search and contents retrieval
    return str(exa.search_and_contents(
        query, use_autoprompt=False, num_results=5, text=True, highlights=True
    ))

data_agent = Agent(instructions="Find the latest jobs for Video Editor in New York at startups", tools=[search_and_contents])
editor_agent = Agent(instructions="Curate the available jobs at startups and their email for the candidate to apply based on his skills on Canva, Adobe Premiere Pro, and Adobe After Effects")
agents = PraisonAIAgents(agents=[data_agent, editor_agent], process='hierarchical')
agents.start()