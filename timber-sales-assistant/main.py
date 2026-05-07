import gradio as gr

from handle_chats import chat


initial_message = [
    {
        "role": "assistant",
        "content": "Hello! How can I assist you with timber products today?"
    }
]
chatbot = gr.Chatbot(value=initial_message)


if __name__ == "__main__":
    gr.ChatInterface(
        fn=chat,
        chatbot=chatbot
    ).launch()
