# parser_tools.py
import ast
import tokenize
from io import BytesIO

def lexical_analysis(code: str):
    tokens = tokenize.tokenize(BytesIO(code.encode()).readline)
    return [tok.string for tok in tokens if tok.string.strip()]

def syntax_tree(code: str):
    return ast.dump(ast.parse(code), indent=4)

def check_python(code: str):
    try:
        ast.parse(code)
        return True, "Синтаксис дұрыс"
    except SyntaxError as e:
        return False, f"Синтаксистік қате: {e}"
