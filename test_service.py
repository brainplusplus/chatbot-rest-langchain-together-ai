import os
import unittest
import time

import pytest

from parameter.answer_question_parameter import AnswerQuestionParameter
from service.implementation.chatbot.chatbot_together_ai_service import ChatbotTogetherAIService

class ChatbotTogetherAIServiceTest(unittest.TestCase):
    def test_service_answer_question_200(self):
        time.sleep(2)
        os.environ["TOGETHER_API_KEY"] = os.environ["TOGETHER_API_KEY_TEMP"]

        parameter = AnswerQuestionParameter(question = "Apa itu pulau bali?")
        chatbot_together_ai_service = ChatbotTogetherAIService()
        output = chatbot_together_ai_service.answer_question(parameter)
        self.assertIn('pulau',output)

    def test_service_answer_question_wrong_key_500(self):
        os.environ["TOGETHER_API_KEY"] = "WRONG KEY"

        with pytest.raises(Exception):
            parameter = AnswerQuestionParameter(question = "Apa itu pulau bali?")
            chatbot_together_ai_service = ChatbotTogetherAIService()
            chatbot_together_ai_service.answer_question(parameter)