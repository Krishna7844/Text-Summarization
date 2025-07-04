from google import genai

client = genai.Client(api_key="AIzaSyAs8EMft6ie2aAsFuZIqghjQdJkIzQ1RBo")
chat = client.chats.create(
    model="gemini-2.5-flash"
    )

def text_summarization(role, message):
# role = "From now on, you are UltraSpark, a superhero with tech powers and a charming sense of humor. Act accordingly in all responses."

    chat.send_message(role)
    response = chat.send_message(message)
    return response.text

role = input("Enter the role you want to assign: ") 
message = input("enter a message: ")
print(text_summarization(role, message))