from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException

from parameter.answer_question_parameter import AnswerQuestionParameter
from service.chatbot_service import ChatbotService
from service.implementation.chatbot.chatbot_together_ai_service import ChatbotTogetherAIService

async def init_chatbot_together_ai_service() -> ChatbotTogetherAIService:
    return ChatbotTogetherAIService()

chatbot_service = Annotated[ChatbotService, Depends(init_chatbot_together_ai_service)]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/answer_question")
async def answer_question(parameter: AnswerQuestionParameter, service: chatbot_service):
    try:
        output = service.answer_question(parameter)
        return {"answer": output}
    except:
        raise HTTPException(
            status_code=500,
            detail="Error",
            headers={"X-Error": "Error"},
        )
    return {"answer": output}

