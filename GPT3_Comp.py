# super simple one-shot prompt w/o resubmitting responses for context

import openai
import jamiemods as jhh # use your key

openai.api_key = jhh.dictOfSecrets['JamieHollowayOpenAI'] # use your key

while True:
    prompt = input("Jamie: ")

    if prompt.find("StopChat") >= 0:
        print(f"\nstopping chat")        
        break
    
    response = openai.Completion.create(engine="text-davinci-003",prompt=prompt,max_tokens=4087,n=1,stop=None,temperature=0.5)
    print(response.choices[0].text)
    
del openai.api_key