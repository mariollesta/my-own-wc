#!/usr/bin/ python


"""
Filename: main.py
Author: Mario Llesta
Fecha de Creación: 18/11/2023

Outline:
This module contains the main code of the mywc tool.
"""

 
# Imports 
import typer, chardet
import sys
from rich import print


app = typer.Typer(rich_markup_mode="rich")


# Functions
@app.command(epilog="Made by [green]mariollesta[/green]")  
def mywc(
    file:str = typer.Argument("", help="File PATH"), 
    c: bool = typer.Option(default=0, show_default=None, help="Print the bytes count", rich_help_panel="Main Options"),
    l: bool = typer.Option(default=0, show_default=None, help="Print the newlines count", rich_help_panel="Main Options"),
    w: bool = typer.Option(default=0, show_default=None, help="Print the words count", rich_help_panel="Main Options"),
    m: bool = typer.Option(default=0, show_default=None, help="Print the characters count", rich_help_panel="Main Options")
):
    
    """
    Outline:
    Print newline, word, and byte counts for a FILE.
    With no FILE, read standard input.
    
    If no input or file is entered, the program will do nothing. 
    In this case, press Ctrl/Cmd + c to stop its execution.
    """
    
    content = 0
    
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
        num_words = len(content.split())
        
        if c:
            print(f"{bytes} {file}")
            
        elif l:
            print(f"{num_lines} {file}")
            
        elif w: 
            print(f"{num_words} {file}")
            
        elif m:
            characters_per_line = 0
            total_characters = 0
            
            encoding_result = chardet.detect(content)
            encoding = encoding_result['encoding']
            
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
                
              
        else:
            print(f"{num_lines} {num_words} {bytes} {file}")
            

    except FileNotFoundError:
        print(f"Error: File not found.")
    
    except Exception as e:
        print(f"Error: {e}")
    


if __name__ == "__main__":
    app()