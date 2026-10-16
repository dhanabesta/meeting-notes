from groq import Groq

client = Groq(
    api_key="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"
)
def call_llm(prompt):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )

    return response.choices[0].message.content