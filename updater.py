def update_hardness_value(e, hardness_value):
    try:
        hardness_value[0] = float(e.control.value)
    except:
        raise ValueError("Invalid value")

def update_source_index(e, source_index):
    source_index[0] = e.control.selected_index