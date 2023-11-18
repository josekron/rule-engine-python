__author__ = "Jose AHP"

def evaluate_condition(condition, data):
    """Evaluate a condition for a rule variable: 
    rule value + operation + data value 
    """
    variable, op, value = condition
    data_value = data.get(variable)

    '''If there is no input data for this condition, then we assume it's True.
    If the input data should have variables for ALL the rule conditions, 
    then this condition should be changed to return False'''
    if data_value is None:
        return True

    if op == "equals":
        return data_value == value
    elif op in ["is above", "greater than"]:
        return data_value > value
    elif op in ["is below", "less than"]:
        return data_value < value
    else:
        raise ValueError("Invalid operator ", op)
    
def parse_condition(line):
    """Parse a rule line to return: variable, operation, value"""
    line_split = line.split(' ')
    first = line_split[0]
    middle = ' '.join(line_split[1:-1])
    last = int(line_split[-1])
    
    return (first, middle, last)
    
def evaluate(rule, data):
    """Main funtion to evaluate if an input data applies to a rule:
    1. Parse line by line of the rule.
    2. If the line is a condition, then check if the input data applies to the condition
       and push the value into the stack.
    3. If the line is a operation (AND, OR, EITHER), then pop from the stack
       and push the new value into the stack.
    4. Return the last value from the stack"""
    stack = []
    current_operator = ''
    lines = rule.strip().split('\n')

    for line in lines:
        line = line.strip()
        if line in ['EITHER', 'AND', 'OR']:
            current_operator = line
            stack.append(line)
        else:
            condition_value = str(evaluate_condition(parse_condition(line), data))

            if current_operator == 'AND':
                stack.pop() # pop 'AND'
                previous_value = stack.pop()
                if(condition_value == 'True' and previous_value == 'True'):
                    stack.append('True')
                else:
                    stack.append('False')
            elif current_operator == 'OR':
                stack.pop() # pop 'OR'
                previous_value = stack.pop()
                stack.pop() # pop 'EITHER'
                if(condition_value == 'True' or previous_value == 'True'):
                    stack.append('True')
                else:
                    stack.append('False')
            else:
                stack.append(str(condition_value))
    
    if len(stack) == 1:
        return True if stack.pop() == 'True' else False
    else: # For the cases we have a rule with AND/OR followed by EITHER
        last_value = stack.pop()
        operator = stack.pop()
        previous_value = stack.pop()

        if operator == 'AND':
            return last_value == 'True' and previous_value == 'True'
        else: # OR
            return last_value == 'True' or previous_value == 'True'