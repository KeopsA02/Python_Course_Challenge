""" Creating nice-looking reports or messages with multiple lines. """

name = "Alice"
score = 95.5
report = f"""
Student Report:
==============
Name: {name}
Score: {score:.1f}%
Status: {'Pass' if score >= 60 else 'Fail'}
"""
print(report)