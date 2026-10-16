from prompt import PROMPT_TEMPLATE
from model import call_llm

print("Meeting Notes Summarizer")

# User input
meeting_notes = input("\nEnter meeting notes:\n\n")

# Create prompt
prompt = PROMPT_TEMPLATE.format(
    meeting_notes=meeting_notes
)

# Send to LLM
response = call_llm(prompt)

# Final Output
print("\nGenerated Summary:\n")

print(response)