import google.generativeai as genai
import PIL.Image
import os
from dotenv import load_dotenv
import requests
from openai import OpenAI
from io import BytesIO
from datetime import datetime

load_dotenv()

apiKeyOpenai = os.getenv("openai_apikey")

client = OpenAI(
    api_key=apiKeyOpenai
)

def generateImageWithDalle(prompt):

    AıResponse = client.images.generate(
        model="dall-e-3",
        size= "1024x1024",
        quality="hd",
        n=1,
        response_format= "url",
        prompt=prompt
    )

    imageUrl = AıResponse.data[0].url

    response = requests.get(imageUrl)
    imageBytes = BytesIO(response.content)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    fileName = f"./img/genareted_Img_{timestamp}.png"

    if not os.path.exists("./img"):
        os.makedirs("./img")

    with open(fileName, "wb") as file:
        file.write(imageBytes.getbuffer())    

    return fileName

apiKeyGoogle = os.getenv("google_apikey")

genai.configure(
    api_key=apiKeyGoogle

)

def geminiVisionWihtLocalFile(imagePath, prompt):

    multimodalityPrompt = f"""Bu gönderdiğim resmi,bazı ek yönergelerle birlikte yeniden oluşturmanı istiyorum.Bunun için ilk olarak resmi son derece ayrıntılı biçimde betimle.Daha sonra sonucunda bana vereceğin metni, bir yapay zeka modelini kullanarak görsel oluşturmakta kullanacağım. O yüzden yanıtına son halini verirken bunun resim üretmekte kullanılacak bir girdi yani prompt oldğunu dikkate al. İşte ek yönerge şöyle: {prompt}
"""
    client = genai.GenerativeModel(model_name="gemini-pro-vision")

    sourceImage = PIL.Image.open(imagePath)

    AıResponse = client.generate_content(
        [
            multimodalityPrompt,
            sourceImage
        ]
    )

    AıResponse.resolve()

    return AıResponse.text

def generateImage(imagePath, prompt):

    imageBasedPrompt = geminiVisionWihtLocalFile(imagePath=imagePath, prompt=prompt)

    fileName = generateImageWithDalle(prompt=imageBasedPrompt)

    return fileName
