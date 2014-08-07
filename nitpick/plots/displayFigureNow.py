from IPython.display import display, clear_output

def displayFigureNow(figure):
    """
    This function displays it's input in IPython immediately.
    It passes it's input through the IPython display system and replaces the current cell output with the displayed input.
    It also waits until the input is ready to be displayed before clearing the current output - this stops everything jumping around.
    """
    
    clear_output(wait=True)
    display(figure)
