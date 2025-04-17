def is_text_empty(text):
    return not text.strip()

def is_not_digit(text):
    return not text.isdigit()

def is_list_empty(lst):
    return not lst

def is_dict_empty(dct):
    return not dct

def are_all_checkboxes_unselected(checkbox_vars):
    return not any(var.get() for var in checkbox_vars)

