from iranagent import IranAgent

def main():
    iranagent = IranAgent(agent_file="agents.yaml")
    return iranagent.run()

if __name__ == "__main__":
    print(main())