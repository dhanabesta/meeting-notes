import streamlit as st

from prompt import PROMPT_TEMPLATE
from model import call_llm

# 📋 Title
st.title("📝 Meeting Notes Summarizer")

# ✍️ Input
meeting_notes = st.text_area(
    "📄 Enter Meeting Notes"
)

# 🚀 Button
if st.button("✨ Generate Summary"):

    if meeting_notes.strip() == "":

        st.warning("⚠️ Please enter meeting notes.")

    else:

        # 🛠️ Create prompt
        prompt = PROMPT_TEMPLATE.format(
            meeting_notes=meeting_notes
        )

        # 🤖 Call LLM
        response = call_llm(prompt)

        # 📑 Display FINAL OUTPUT
        st.subheader("📌 Generated Summary")

        st.write(response)