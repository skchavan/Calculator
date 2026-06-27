def calculate(expression):
    """
    Evaluate a mathematical expression.
    """

    try:
       return eval (expression)
    except ZeroDivisionError:
        return "Error: Division by Zero"
    except Exception:
        return "Error"