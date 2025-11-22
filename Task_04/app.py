import chainlit as cl
from chainlit import Message, File
from agent import main_agent
from agents import Runner
from utils import extract_text_from_pdf
from openai.types.responses import ResponseTextDeltaEvent
import os
from pathlib import Path


@cl.on_chat_start
async def on_chat_start():
    """Initialize the chat session"""
    cl.user_session.set("agent", main_agent)
    cl.user_session.set("pdf_text", None)

    await cl.Message(
        content="Hello! 👋 I'm your PDF Assistant. Upload a PDF document and I'll help you understand it by:\n"
        "- Providing a clear summary\n"
        "- Generating quizzes to test your knowledge\n\n"
        "Just upload a PDF to get started!"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    """Handle incoming messages and PDF uploads"""
    agent = cl.user_session.get("agent")

    # Handle PDF uploads
    if message.elements:
        for element in message.elements:
            if isinstance(element, File) and element.mime == "application/pdf":
                await cl.Message(content="📄 Processing your PDF...").send()

                # In newer Chainlit versions, use element.path instead of element.content
                if element.path:
                    # Use the existing path
                    pdf_text = extract_text_from_pdf(element.path)
                elif element.content:
                    # Fallback: if content is provided (older versions)
                    temp_pdf_path = Path("temp_uploaded_pdf.pdf")
                    with open(temp_pdf_path, "wb") as f:
                        f.write(element.content)
                    pdf_text = extract_text_from_pdf(str(temp_pdf_path))
                    os.remove(temp_pdf_path)
                else:
                    await cl.Message(
                        content="❌ Error: Could not access PDF file"
                    ).send()
                    return

                # Store PDF text in session for future reference
                cl.user_session.set("pdf_text", pdf_text)

                # Create user message with PDF context
                user_message = f"I've uploaded a PDF document. Here's the content:\n\n{pdf_text}\n\nPlease summarize this document for me."

                # Stream the agent's response
                response_msg = cl.Message(content="")
                await response_msg.send()

                try:
                    # Use streaming for real-time response
                    result = Runner.run_streamed(agent, user_message)

                    full_response = ""
                    async for event in result.stream_events():
                        # Only handle text delta events for streaming to user
                        if event.type == "raw_response_event" and isinstance(
                            event.data, ResponseTextDeltaEvent
                        ):
                            token = event.data.delta
                            full_response += token
                            await response_msg.stream_token(token)

                    # Finalize the message to stop loading animation
                    await response_msg.update()

                except Exception as e:
                    await response_msg.remove()
                    await cl.Message(content=f"❌ Error: {str(e)}").send()

                return

    # Handle regular text messages (including quiz requests)
    if message.content:
        pdf_text = cl.user_session.get("pdf_text")

        # Build the user message
        if pdf_text and (
            "quiz" in message.content.lower()
            or "test" in message.content.lower()
            or "yes" in message.content.lower()
        ):
            # If user is asking for a quiz and we have PDF text
            user_message = f"{message.content}\n\nPDF Content:\n{pdf_text}"
        else:
            user_message = message.content

        # Stream the response
        response_msg = cl.Message(content="")
        await response_msg.send()

        try:
            # Use streaming for real-time response
            result = Runner.run_streamed(agent, user_message)

            full_response = ""
            async for event in result.stream_events():
                # Only handle text delta events for streaming to user
                if event.type == "raw_response_event" and isinstance(
                    event.data, ResponseTextDeltaEvent
                ):
                    token = event.data.delta
                    full_response += token
                    await response_msg.stream_token(token)

            # Finalize the message to stop loading animation
            await response_msg.update()

        except Exception as e:
            await response_msg.remove()
            await cl.Message(content=f"❌ Error: {str(e)}").send()
