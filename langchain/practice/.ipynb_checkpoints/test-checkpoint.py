from langchain_openai.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()

model = OpenAI(model = 'gpt-3.5-turbo-instruct')
result = model.invoke('한국의 수도는')
print(result)