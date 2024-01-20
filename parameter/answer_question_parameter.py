from pydantic import BaseModel
from typing import Optional

class AnswerQuestionParameter(BaseModel):
    question: str
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 128
    top_k: Optional[int] = 50