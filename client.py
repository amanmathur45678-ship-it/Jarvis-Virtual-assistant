


from google import genai

client = genai.Client(api_key="Your api key")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="your contents"
)

print(response.text)
