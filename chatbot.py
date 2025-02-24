import google.generativeai as genai
genai.configure(api_key="AIzaSyCqzg8gsPatLWudhFOr7anQHc2q6ifTvAg")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
while True:
    soru = input("Siz: ")
    if soru.lower() == "exit":
        print(("Coded By Atn_Naz"))
        break
    cevap = chat.send_message(soru)
    print("Chatbot:", cevap.text)