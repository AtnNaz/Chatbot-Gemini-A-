import google.generativeai as genai
genai.configure(api_key="YOUR APİ KEY")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
while True:
    soru = input("Siz: ")
    if soru.lower() == "exit":
        print(("Coded By Atn_Naz"))
        break
    cevap = chat.send_message(soru)
    print("Chatbot:", cevap.text)
