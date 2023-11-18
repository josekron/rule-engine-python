from rule_engine import *

rule = """
EITHER
    credit_rating is above 50
    AND
    flood_risk is below 10
OR
    revenue is above 1000000
"""

print('Evaluating rule:\n', rule)

assert evaluate(rule,  {
    'credit_rating': 10,
    'flood_risk': 9,
    'revenue': 20000000
}) == True

assert evaluate(rule,  {
    'credit_rating': 10,
    'flood_risk': 9,
    'revenue': 100
}) == False

assert evaluate(rule,  {
    'credit_rating': 10,
    'flood_risk': 20,
    'revenue': 20000000
}) == True

assert evaluate(rule,  {
    'credit_rating': 60,
    'flood_risk': 10,
    'revenue': 100
}) == False

rule = """
credit_rating is above 50
AND
flood_risk is below 10
"""

print('\nEvaluating rule:\n', rule)

assert evaluate(rule,  {
    'credit_rating': 100,
    'flood_risk': 9,
}) == True

assert evaluate(rule,  {
    'credit_rating': 10,
    'flood_risk': 10,
}) == False

rule = """
credit_rating is above 50
AND
EITHER
    flood_risk is below 10
OR
    revenue is above 1000000
"""

print('\nEvaluating rule:\n', rule)

assert evaluate(rule,  {
    'credit_rating': 100,
    'flood_risk': 20,
    'revenue': 2000000
}) == True

assert evaluate(rule,  {
    'credit_rating': 10,
    'flood_risk': 9,
    'revenue': 2000000
}) == False

assert evaluate(rule,  {
    'credit_rating': 10,
    'flood_risk': 20,
    'revenue': 100
}) == False

rule = """
credit_rating is above 50
AND
flood_risk equals 10
"""

print('\nEvaluating rule:\n', rule)

assert evaluate(rule,  {
    'credit_rating': 100,
    'flood_risk': 10
}) == True

assert evaluate(rule,  {
    'credit_rating': 100,
    'flood_risk': 100
}) == False