# programa de python 
import os
import sys

DEFAULT_FILENAME = "word.txt"

def sort_list(item, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")
    
    return sorted(items, reverse=(not ascending))