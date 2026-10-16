


from google import genai

client = genai.Client(api_key="Your api key")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="me apko integrate nahi kar paa rha hu apne jarvis project me kaise integrate kar sakta hau"
)

print(response.text)


