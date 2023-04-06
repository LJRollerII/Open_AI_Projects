import openai

# Generate Image

openai.api_key = open("API_KEY", "r").read()

response = openai.Image.create(
    prompt="a white siamese cat",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']

print(response['data'])

print(image_url)