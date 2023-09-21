def display_progress_bar(percentage_done):
    total_chars = 20
    done_chars = int(total_chars * percentage_done / 100)
    remaining_chars = total_chars - done_chars
    progress_bar = '[' + '/' * done_chars + '-' * remaining_chars + ']'
    print(progress_bar, f"{percentage_done}%")
