
def evaluate_rule(rule_ast, data):
    if rule_ast.type == 'operator':
        left_result = evaluate_rule(rule_ast.left, data)
        right_result = evaluate_rule(rule_ast.right, data)
        if rule_ast.value == 'AND':
            return left_result and right_result
        elif rule_ast.value == 'OR':
            return left_result or right_result
    elif rule_ast.type == 'operand':
        left_operand, operator, right_operand = rule_ast.value
        user_value = data.get(left_operand)
        if operator == '>':
            return user_value > right_operand
        elif operator == '<':
            return user_value < right_operand
        elif operator == '=':
            return user_value == right_operand
    return False
