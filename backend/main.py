import io 
from fastapi import FastAPI, HTTPException, UploadFile, File, Form 
import base64 
from PIL import Image 
from ai_engine import get_diagnosis
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Porichorja API', description='Plant Disease Detection API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/diagnose")
async def diagnose_plant(
    image: UploadFile = File(None),
    symptoms: str = Form("")
):
    if not image and not symptoms.strip():
        raise HTTPException(status_code=400, detail="দয়া করে ছবি অথবা লক্ষণ—যেকোনো একটি প্রদান করুন।")

    if image and not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="অনুগ্রহ করে একটি ছবি আপলোড করুন।")

    try:
        image_path = None
        if image:
            # Read image file
            image_bytes = await image.read()
            img = Image.open(io.BytesIO(image_bytes))
            img.thumbnail((800, 800))
            
            # Save image temporarily
            image_path = "temp_image.jpg"
            img.convert("RGB").save(image_path, "JPEG")
        
        # Get diagnosis from AI engine
        diagnosis = get_diagnosis(image_path, symptoms)
        
        # Clean up temporary file
        if image_path:
            import os
            os.remove(image_path)
        
        return {
            "status": "success",
            "diagnosis": diagnosis
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


