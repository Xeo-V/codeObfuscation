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

