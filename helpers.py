from termcolor import colored


def env_config():
    token = input(colored("Bot Token: ", "cyan"))
    with open(f'.env', 'w') as wr:
        wr.write(f"TOKEN=\'{token}\'\n")
