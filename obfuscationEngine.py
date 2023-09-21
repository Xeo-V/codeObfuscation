import random
import re

def display_progress_bar(percentage_done):
    total_chars = 20
    done_chars = int(total_chars * percentage_done / 100)
    remaining_chars = total_chars - done_chars
    progress_bar = '[' + '/' * done_chars + '-' * remaining_chars + ']'
    print(progress_bar, f"{percentage_done}%")


def obfuscate_file_with_progress(filename, mode='manual'):
    print("Starting obfuscation...")
    display_progress_bar(0)
    with open(filename, 'r') as file:
        content = file.read()
    display_progress_bar(30)
    if mode == 'manual':
        obfuscated_content = obfuscate_manual(content)
    elif mode == 'underscores':
        obfuscated_content = obfuscate_with_underscores(content)
    else:
        raise ValueError("Invalid obfuscation mode.")
    display_progress_bar(70)
    with open(filename.replace('.py', '_obfuscated.py'), 'w') as file:
        file.write(obfuscated_content)
    display_progress_bar(100)
    print(f"Obfuscated file saved as {filename.replace('.py', '_obfuscated.py')}")

def obfuscate_manual(content):
    content = re.sub(r'(\w+)', lambda x: x.group(1)[::-1], content)
    return content

def obfuscate_with_underscores(content):
    words = set(re.findall(r'\b\w+\b', content))
    
    python_keywords = set([
        "False", "None", "True", "and", "as", "assert", "async", "await",
        "break", "class", "continue", "def", "del", "elif", "else", "except",
        "finally", "for", "from", "global", "if", "import", "in", "is",
        "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try",
        "while", "with", "yield"
    ])
    
    python_builtins = set([
        "abs", "all", "any", "ascii", "bin", "bool", "bytearray", "bytes", "callable", "chr",
        "classmethod", "compile", "complex", "delattr", "dict", "dir", "divmod", "enumerate", 
        "eval", "exec", "filter", "float", "format", "frozenset", "getattr", "globals", 
        "hasattr", "hash", "help", "hex", "id", "input", "int", "isinstance", "issubclass", 
        "iter", "len", "list", "locals", "map", "max", "memoryview", "min", "next", "object", 
        "oct", "open", "ord", "pow", "print", "property", "range", "repr", "reversed", "round", 
        "set", "setattr", "slice", "sorted", "staticmethod", "str", "sum", "super", "tuple", 
        "type", "vars", "zip"
    ])

    exclude_set = python_keywords.union(python_builtins)
    words = words - exclude_set

    obfuscated_words = {}
    for idx, word in enumerate(sorted(list(words))):
        obfuscated_word = '_' * (3 + idx)
        obfuscated_words[word] = obfuscated_word

    for original, obfuscated in obfuscated_words.items():
        content = content.replace(original, obfuscated)
    return content


if __name__ == "__main__":
    filename = input("Enter the Python file to obfuscate: ")
    mode = input("Choose obfuscation mode (manual/underscores): ")
    obfuscate_file_with_progress(filename, mode)
