from fastapi.testclient import TestClient
import os

from main import app

client = TestClient(app)

def test_answer_question_200():
    os.environ["TOGETHER_API_KEY"] = os.environ["TOGETHER_API_KEY_TEMP"]
    response = client.post(
        "/answer_question",
        json={
          "question": "Apa itu pulau bali?",
          "temperature": 0.7,
          "max_tokens": 128,
          "top_k": 50
        },
    )
    assert response.status_code == 200

def test_answer_question_wrong_key_500():
    os.environ["TOGETHER_API_KEY"] = "WRONG KEY"

    response = client.post(
        "/answer_question",
        json={
          "question": "Apa itu pulau bali?",
          "temperature": 0.7,
          "max_tokens": 128,
          "top_k": 50
        },
    )
    assert response.status_code == 500

