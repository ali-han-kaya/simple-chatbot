import pytest
from simple_chatbot import get_response

# Test fonksiyonu
def test_get_response():
    # Test senaryoları
    assert get_response("Hello") == "Hi! How can I assist you?"
    assert get_response("How are you?") == "I'm an AI, so I don't have feelings, but I'm here to help you!"
    assert get_response("What's your name?") == "I am a chatbot. I don't have a name, but it's nice to meet you."
    assert get_response("Random input") == "Sorry, I didn't understand that. Feel free to ask something else."

