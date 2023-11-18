### Description

Rule engine that accepts a rule in a natural language and validates if the input data passes the condition.

- Rule format:

```python
EITHER
  water_level is above 50
  AND
  air_level is below 10
OR
  cost_device is above 1000000
```

- Input:

```python
EXAMPLE_1 = {
    "water_level": 75,
    "air_level": 5,
    "cost_device": 1000
}
```

- Output:

```python
True
```

### Assumptions

If there is no input data for a specific rule condition, then we assume the input data passes the condition. E.g:

- Rule:

```python
water_level is above 50
AND
air_level is below 10
```

- Input:

```python
EXAMPLE_1 = {
    "cost_device": 1000
}
```

`water_level` and `air_level` are not in the input data, so it passes the rule.

If the input data should contain variables for ALL the rule conditions, then we should change the `line 14` to `False` in `rule_engine.py`.
