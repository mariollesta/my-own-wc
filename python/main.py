import typer
from rich import print


def main(name: str, lastname: str = "", formal: bool = False):
    """
    Say hi to NAME, optionally with --lastname.
    
    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Good day Mr. {name} {lastname}.")    
    else:
        print(f"Hello, {name} {lastname}")



if __name__ == "__main__":
    typer.run(main)