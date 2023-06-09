import openai

# Edit Image

openai.api_key = open("API_KEY", "r").read()

response = openai.Image.create_edit(
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="a sunlit indoor lounge area with a pool containing a flamingo",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']

print(response['data'])

print(image_url)