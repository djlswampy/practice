from langchain_openai.llms import OpenAI

model = OpenAI(model = 'gpt-3.5-turbo-instruct')

model.invoke('한국의 수도는')