import base64 
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
token = os.getenv("HF_TOKEN")
client = InferenceClient(token=token)

def traslate_diagnosis(diagnosis):
    model = "Qwen/Qwen3-235B-A22B"
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Translate the following text to Bangla: " + diagnosis},
            ],
        }
    ]
    response = client.chat_completion(
        messages=messages,
        max_tokens=500,
        model=model
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content



def get_diagnosis(image_path, user_text_bangla):

    image_url = None
    if image_path:
        # Convert image to base64 for image transmission
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        image_url = f"data:image/jpeg;base64,{encoded_image}"

    # Construct the prompt for the model
    if image_path and user_text_bangla:
        prompt = f"""
        You are a helpful assistant that can diagnose plant diseases based on images and user descriptions.
        The user has provided an image of a plant and a description in Bangla.
        Please analyze the image identify the plant and based on the description provide a diagnosis.
        
        User Description: {user_text_bangla}
        """
    elif image_path:
        prompt = """
        You are a helpful assistant that can diagnose plant diseases based on images.
        The user has provided an image of a plant.
        Please analyze the image identify the plant and provide a diagnosis.
        """
    else:
        prompt = f"""
        You are a helpful assistant that can diagnose plant diseases based on user descriptions.
        The user has provided a description in Bangla.
        Please provide a diagnosis based on this description.
        
        User Description: {user_text_bangla}
        """
    
    prompt += """
    Please provide the diagnosis in the following format:
    
    Disease: [Name of the disease]
    Symptoms: [Description of the symptoms]
    Treatment: [Recommended treatment]
    """

    content = [{"type": "text", "text": prompt}]
    if image_url:
        content.append({"type": "image_url", "image_url": {"url": image_url}})

    messages = [
        {
            "role": "user",
            "content": content,
        }
    ]

    response = client.chat_completion(
        messages=messages,
        max_tokens=500,
        model="Qwen/Qwen2.5-VL-7B-Instruct"
    )

    print(response.choices[0].message.content)

    return response.choices[0].message.content

