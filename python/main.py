import typer
from rich import print


app = typer.Typer()

@app.command()  
def main(name: str, lastname: str = "", formal: bool = False):
    """
    Say hi to NAME, optionally with --lastname.
    
    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Good day Mr. {name} {lastname}.")    
    else:
        print(f"Hello, {name} {lastname}")

@app.command()  
def mywc(
    file, 
    c: bool = typer.Option(False, help="Print the bytes count"),
    l: bool = typer.Option(False, help="Print the newlines count")
):
    try:
        with open(file, 'rb') as f:
            content = f.read()
            
            if c:
                bytes = len(content)
                print(f"{bytes} {file}")
                
            if l:
                lines = content.count(b'\n')
                print(f"{lines} {file}")
    
    except FileNotFoundError:
        print(f"File {file} not found.")
    
    except Exception as e:
        print(f"Error: {e}")
    


if __name__ == "__main__":
    app()