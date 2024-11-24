
from fastapi import FastAPI
from pydantic import BaseModel 
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import HuggingFacePipeline
from model import model

memory = ConversationBufferMemory()
llm = HuggingFacePipeline(pipeline=model)
chat = ConversationChain(llm=llm, memory=memory)

def chat_with_bot(user_input):
    return chat.run(user_input)


app = FastAPI()

class UserInput(BaseModel):
    message: str

@app.post("/chat")
async def chatbot(input: UserInput):
    response = chat_with_bot(input.message)
    return {"response": response}

