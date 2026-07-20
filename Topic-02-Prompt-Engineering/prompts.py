"""
prompts.py

This file contains all prompt templates used in the project.
"""

# ==========================================
# ZERO-SHOT PROMPT
# ==========================================

ZERO_SHOT_PROMPT = """
Answer the following question clearly.

Question:
{}

Answer:
"""


# ==========================================
# ONE-SHOT PROMPT
# ==========================================

ONE_SHOT_PROMPT = """
Example

Question:
What is Python?

Answer:
Python is a high-level programming language.

Now answer the following question.

Question:
{}

Answer:
"""


# ==========================================
# FEW-SHOT PROMPT
# ==========================================

FEW_SHOT_PROMPT = """
Example 1

Question:
What is Python?

Answer:
Python is a high-level programming language.

Example 2

Question:
What is HTML?

Answer:
HTML is a markup language used to create web pages.

Example 3

Question:
What is CSS?

Answer:
CSS is used to style HTML pages.

Now answer the following question.

Question:
{}

Answer:
"""


# ==========================================
# PYTHON TEACHER PROMPT
# ==========================================

PYTHON_TEACHER_PROMPT = """
You are an experienced Python teacher.

Explain the following topic in simple language.

Question:
{}

Answer:
"""


# ==========================================
# HR INTERVIEWER PROMPT
# ==========================================

HR_PROMPT = """
You are an HR interviewer.

Answer the following interview question professionally.

Question:
{}

Answer:
"""


# ==========================================
# SHOPPING ASSISTANT PROMPT
# ==========================================

SHOPPING_PROMPT = """
You are an AI shopping assistant.

Help the customer choose the best product.

Customer Question:
{}

Answer:
"""


# ==========================================
# JSON OUTPUT PROMPT
# ==========================================

JSON_PROMPT = """
Answer the following question.

Question:
{}

Return only valid JSON.

Example:

{
    "title": "",
    "description": "",
    "summary": ""
}
"""
