from ast_builder import Node

def combine_rules(rule_asts):
    if len(rule_asts) == 1:
        return rule_asts[0]

    combined_rule = rule_asts[0]
    for rule in rule_asts[1:]:
        combined_rule = Node('operator', left=combined_rule, right=rule, value='AND')
    
    return combined_rule

