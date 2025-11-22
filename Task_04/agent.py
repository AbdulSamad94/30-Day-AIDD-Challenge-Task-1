import os
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel, AsyncOpenAI
from agents import Agent
from prompts import main_agent_prompt, summarizer_prompt, quiz_generator_prompt

load_dotenv()

# Initialize the Gemini client
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# Initialize the OpenaiChatCompletionModel with the Gemini model
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

# Create specialized agents for summarization and quiz generation
summarizer_agent = Agent(
    name="PDF Summarizer",
    instructions=summarizer_prompt,
    model=model,
)

quiz_generator_agent = Agent(
    name="Quiz Generator",
    instructions=quiz_generator_prompt,
    model=model,
)

# Create the main orchestrator agent that uses sub-agents as tools
main_agent = Agent(
    name="PDF Assistant",
    instructions=main_agent_prompt,
    model=model,
    tools=[
        summarizer_agent.as_tool(
            tool_name="summarize_pdf",
            tool_description="Summarizes the uploaded PDF document in a structured format with key points and insights.",
        ),
        quiz_generator_agent.as_tool(
            tool_name="generate_quiz",
            tool_description="Generates a comprehensive quiz with multiple-choice questions (MCQs) based on the PDF content. Each question has 4 options with the correct answer highlighted.",
        ),
    ],
)
