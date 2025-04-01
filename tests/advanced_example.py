from iranagent import IranAgent

def advanced():
    iranagent = IranAgent(
        framework="autogen",
        auto=True,
        task="create a movie script about a robot in Mars",
        tools=["search", "code"]
    )
    print(iranagent)
    return iranagent.run()

if __name__ == "__main__":
    print(advanced())