import typer, chardet
import sys
from rich import print


app = typer.Typer()


@app.command()  
def mywc(
    file:str = typer.Argument("", help="File PATH"), 
    c: bool = typer.Option(False, help="Print the bytes count"),
    l: bool = typer.Option(False, help="Print the newlines count"),
    w: bool = typer.Option(False, help="Print the words count"),
    m: bool = typer.Option(False, help="Print the characters count")
):
    
    """
    Print newline, word, and byte counts for a FILE.
    With no FILE, read standard input.
    """
    try:
        
        if file:
            with open(file, 'rb') as f:
                content = f.read()
        else:
            content = sys.stdin.buffer.read()
                
             
        if c:
            bytes = len(content)
            print(f"{bytes} {file}")
            
        elif l:
            lines = content.count(b'\n')
            print(f"{lines} {file}")
            
        elif w: 
            words = content.split()
            print(f"{len(words)} {file}")
            
        elif m:
            encoding_result = chardet.detect(content)
            encoding = encoding_result['encoding']
            
            try:
                with open(file, 'r', encoding=encoding) as tmp: 
                    line_breaks = 0
                    characters_per_line = 0
                    total_characters = 0
                    
                    lines = tmp.readlines()
                    line_breaks = len(lines)
                    
                    for line in lines:
                        characters_per_line += len(line)
                    
                    total_characters = characters_per_line + line_breaks + 1
                    
                    print(f"{total_characters} {file}")
                
            except Exception as e:
                print(f"Error: {e}")    
        
        else:
            lines = content.count(b'\n')
            words = len(content.split())
            bytes = len(content)
            print(f"{lines} {words} {bytes} {file}")

    except FileNotFoundError:
        print(f"Error: File not found.")
    
    except Exception as e:
        print(f"Error: {e}")
    


if __name__ == "__main__":
    app()