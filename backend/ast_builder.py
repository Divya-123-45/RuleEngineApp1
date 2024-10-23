import ast

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type
        self.left = left
        self.right = right
        self.value = value

    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None,
        }

def create_rule(rule_string):
    # Replace 'AND' and 'OR' with Python's 'and' and 'or' for valid syntax
    rule_string = rule_string.replace('AND', 'and').replace('OR', 'or')
    tree = ast.parse(rule_string, mode='eval')
    return build_ast(tree.body)

def build_ast(node):
    if isinstance(node, ast.BoolOp):
        op_type = 'AND' if isinstance(node.op, ast.And) else 'OR'
        left = build_ast(node.values[0])
        right = build_ast(node.values[1])
        return Node(node_type='operator', left=left, right=right, value=op_type)
    elif isinstance(node, ast.Compare):
        left = build_ast(node.left)
        right = build_ast(node.comparators[0])
        op = node.ops[0]
        operator = '>'
        if isinstance(op, ast.Lt):
            operator = '<'
        elif isinstance(op, ast.GtE):
            operator = '>='
        return Node(node_type='operand', value=(left.value, operator, right.value))
    elif isinstance(node, ast.Constant):
        return Node(node_type='value', value=node.value)
    elif isinstance(node, ast.Name):
        return Node(node_type='value', value=node.id)
    else:
        raise ValueError('Invalid rule format')
