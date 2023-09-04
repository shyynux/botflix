import os
from netflix_api.netflix_functions import fetch_netflix_datas
from textbase import bot, Message
from textbase.models import OpenAI
from textbase.message import Content
from typing import List
import json

# Load your OpenAI API key
# OpenAI.api_key = ""
# or from environment variable:
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Initial system message
initial_message = "You are chatting with Botflix, your personal Netflix TV show recommendation bot. I'll help you find the perfect show to watch! If you have any questions or need recommendations, feel free to ask."

@bot()
def on_message(message_history: List[Message], state: dict = None):

 # Check if the user's message contains a search query
    user_message = message_history[-1]
    if "recommend" in user_message:
        # Extract the search query
        search_query = extract_search_query(user_message)

        if search_query:
            # Call the Netflix API with the search query
            netflix_response = fetch_netflix_datas(search_query)

            if netflix_response:
                # Netflix API returns a valid JSON response
                response_text =json.dumps(netflix_response),
                content_list = [
                    Content(data_type="string", value=response_text)
                ],
                user_message = Message(role="system", content=content_list),
                current_response = "Botflix is curating a list, here's what you wanted for {search_query}",
                bot_response = OpenAI.generate(
                    system_prompt=current_response,
                    message_history=user_message,
                    model="gpt-3.5-turbo"
                )
            else:
                # Handle the case when the API response is None
                  bot_response = OpenAI.generate(
                    model="gpt-3.5-turbo",
                    messages=message_history + [{"role": "user", "content": user_message}],
                )
        else:
            # Handle the case when there's no valid search query
            response_text = "What was the genre you wanted? Can you tell me?"
            bot_response = OpenAI.generate(
                system_prompt=response_text,
                message_history=message_history,
                model="gpt-3.5-turbo"
            )
    else:
        # Handle messages that don't contain search queries
        response_text = "Hello! How can I assist you with TV show recommendations today?"
        bot_response = OpenAI.generate(
            system_prompt=response_text,
            message_history=message_history,
            model="gpt-3.5-turbo"
        )

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=initial_message,
        message_history=message_history,
        model="gpt-3.5-turbo"
    )


    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }


def extract_search_query(user_message):
    # Convert the user's message to lowercase for case-insensitive matching
    user_message = user_message.lower()

    # Define a set of common recommendation keywords
    recommendation_keywords = ["recommend", "suggest", "give me", "show me", "find"]

    # Initialize the search query
    search_query = ""

    # Iterate through the keywords and find the first one that appears in the message
    for keyword in recommendation_keywords:
        if keyword in user_message:
            # Split the message by the keyword
            parts = user_message.split(keyword, 1)
            if len(parts) > 1:
                # Extract everything after the keyword as the search query
                search_query = parts[1].strip()
                break

    return search_query
