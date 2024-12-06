from test.add import NeededFunc;NeededFunc()
from src.common.config import IMAGES_DIR
from groq import Groq
import base64 , time

dir_path = os.path.join(IMAGES_DIR, 'images.jpg')
client = Groq(api_key="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")

vision_prompt_text = ('''You are a vision analysis AI designed to extract semantic information from images, focusing on screenshots and webcam captures. Your goal is to provide concise, detailed descriptions that include:
1. Exact text in the image
2. Contextual elements and their significance
3. Screen contents, interface details, and composition
4. Relevant metadata or insights

Generate a neutral, single-paragraph description that highlights key elements relevant to the user's query, providing context for another AI to craft a final response. Avoid assumptions or irrelevant details; focus only on factual, observable information directly related to the prompt.''')

start_time = time.perf_counter()
# Function to encode the image
with open(dir_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')
image_encoding_time = time.perf_counter() - start_time
print(f"Image encoding took {image_encoding_time:.6f} seconds")

chat_completion = client.chat.completions.create(
    messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text":vision_prompt_text},
                {
                    "type": "image_url",
                    "image_url": {

                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    model="llama-3.2-90b-vision-preview",
)

completion_time = time.perf_counter()
print(chat_completion.choices[0].message.content)
print(f"Completion took {completion_time - start_time:.2f} seconds")

