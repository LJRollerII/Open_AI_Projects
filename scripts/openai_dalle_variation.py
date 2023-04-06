import openai

# Edit Image

openai.api_key = open("API_KEY", "r").read()

response = openai.Image.create_variation(
    image=open("corgi_and_cat_paw.png", "rb"),
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']

print(response['data'])

print(image_url)