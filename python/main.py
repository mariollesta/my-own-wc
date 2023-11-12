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
                content = f.read() # bytes
                       
        else:
            content = sys.stdin.buffer.read() # bytes
        
        
        bytes = 0
        num_lines = 0
        num_words = 0
        
        bytes = len(content)
        num_lines = content.count(b'\n') 
        num_words = content.split()
          
        if c:
            print(f"{bytes} {file}")
            
        elif l:
            print(f"{num_lines} {file}")
            
        elif w: 
            print(f"{len(num_words)} {file}")
            
        elif m:
            characters_per_line = 0
            total_characters = 0
            
            encoding_result = chardet.detect(content)
            encoding = encoding_result['encoding']
            
            try:
                if file:      
                    with open(file, 'r', encoding=encoding) as tmp: 
                        lines = tmp.readlines()
                            
                else:
                    lines = content.decode(encoding)
                    num_lines = 0 # line breaks are already included in each line length
                
                for line in lines:
                        characters_per_line += len(line)
                        
                total_characters = characters_per_line + num_lines + 1
                print(f"{total_characters} {file}")
                
            except Exception as e:
                print(f"Error: {e}")    
        
        else:
            print(f"{num_lines} {num_words} {bytes} {file}")

    except FileNotFoundError:
        print(f"Error: File not found.")
    
    except Exception as e:
        print(f"Error: {e}")
    


if __name__ == "__main__":
    app()