from iranagent import IranAgent

def main():
    iranagent = IranAgent(
        framework="autogen",
        auto=True,
        task="create a movie script about a robot in Mars"
    )
    print(iranagent.framework)
    return iranagent.run()

if __name__ == "__main__":
    print(main())