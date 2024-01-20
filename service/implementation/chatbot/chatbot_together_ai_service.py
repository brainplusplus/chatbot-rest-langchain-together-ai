from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.llms import Together
from langchain_core.runnables.utils import Output

from parameter.answer_question_parameter import AnswerQuestionParameter
from service.chatbot_service import ChatbotService


class ChatbotTogetherAIService(ChatbotService):
    def answer_question(self, parameter: AnswerQuestionParameter) -> Output:
        model = Together(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            temperature=parameter.temperature,
            max_tokens=parameter.max_tokens,
            top_k=parameter.top_k
        )

        template = """<s>[INST] {question} [/INST] 
        """
        prompt = ChatPromptTemplate.from_template(template)

        chain = (
                {"question": RunnablePassthrough()}
                | prompt
                | model
                | StrOutputParser()
        )

        input_query = parameter.question
        output = chain.invoke(input_query)
        return output
