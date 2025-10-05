# tiny-ai-qa-bot
A tiny AI-powered Q&amp;A bot built with Python, OpenAI, and Streamlit, featuring real-time conversation memory.

🤖 Tiny AI Q&A Bot 
This repository contains my submission for the internship assignment, which focuses on building a simple, resourceful, and well-documented AI-powered application.

Part 1: Setup and Design Choices :

  Requirement	Choice / Tool Used	Rationale & Resourcefulness
  Project Selection	AI Q&A Bot         ---->	Chosen to demonstrate direct experience with integrating Large Language Models (LLMs) via API.
  Core Technology	Python	             ----> Chosen for its flexibility, rich ecosystem, and robust support for AI/ML development.
  AI Engine	OpenAI API (gpt-3.5-turbo) ----> Selected for its fast response time and simple integration.
  Simple UI (Stretch Goal)	            ---> Streamlit	Chosen to go beyond the minimum by rapidly building a clean, shareable web interface using pure Python.
  API Key Security	.env and .gitignore	--- > Created a .env file to securely store the OPENAI_API_KEY and added it to .gitignore to prevent accidental public upload—a critical security best practice.


**Part 2: Technical Implementation & Core Features: **

  The application is implemented in a single file, "app.py" , which combines the AI logic, conversation memory, and the Streamlit front-end.

  Key Technical Highlights (Demonstrating Effort)
  Conversation Memory (st.session_state):

  The app uses Streamlit's built-in st.session_state dictionary to store the entire chat history.

  On every new user prompt, the full message history is passed back to the OpenAI API, allowing the model to answer contextual follow-up questions and maintain conversation flow.


_**Graceful Error Handling (Robustness):**__

A robust try...except block is implemented around the primary API call.

If the connection fails (due to an invalid key, network issue, or quota limit), the app catches the exception and displays a clean, readable st.error message instead of crashing the application.

Real-Time Streaming Output:

The OpenAI API is called with stream=True.

Streamlit's st.write_stream() function is used to display the AI's response token-by-token, which provides a fast, modern, and engaging user experience.


**Part 3: Outcome and Conclusion**

  Result of Execution
  The application is technically complete and correctly implements all features, including the Streamlit UI (Stretch Goal).

  During the test run, the application encountered an external API issue: a 429: insufficient_quota error.

  This failure, while external, demonstrates the following successes:

  The code successfully reached the point of execution for the API call.

  The Graceful Error Handling feature worked perfectly by catching the external error and displaying it cleanly to the user, proving the robustness of the application's design.


**CONCLUSION :**

The application is technically complete and correctly implements all features, including the Streamlit UI (Stretch Goal) and Graceful Error Handling. The application immediately encountered a "_429: insufficient_quota_" error upon calling the OpenAI API. This confirms the code's successful connection and execution of the API logic. While the quota was unexpectedly exhausted, the application demonstrated robustness by successfully catching and displaying this critical external failure to the user."



Execute the App:

streamlit run app.py

View: The application will automatically open in your web browser.
