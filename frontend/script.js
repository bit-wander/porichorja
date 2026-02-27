async function analyzePlant() {
    const imageInput = document.getElementById('imageInput');
    const symptomsInput = document.getElementById('symptomsInput');
    const btnText = document.getElementById('btnText');
    const resultContainer = document.getElementById('resultContainer');
    const diagnosisText = document.getElementById('diagnosisText');
    const loader = document.getElementById('loader');
    const placeholderResult = document.getElementById('placeholderResult');

    // 1. Validation
    if (!imageInput.files[0] && !symptomsInput.value.trim()) {
        alert("দয়া করে ছবি অথবা লক্ষণ—যেকোনো একটি প্রদান করুন।");
        return;
    }

    // 2. Prepare Form Data
    const formData = new FormData();
    if (imageInput.files[0]) {
        formData.append('image', imageInput.files[0]);
    }
    formData.append('symptoms', symptomsInput.value);

    // 3. UI State: Loading
    loader.classList.remove('hidden');
    resultContainer.classList.add('hidden');
    if (placeholderResult) placeholderResult.classList.add('hidden');
    btnText.disabled = true;
    btnText.innerText = "প্রসেসিং হচ্ছে...";

    try {
        // 4. Call FastAPI Backend
        const response = await fetch('http://127.0.0.1:8000/diagnose', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        console.log(data);
        
        if (data.status === "success") {
            // console.log(data.diagnosis);
            diagnosisText.innerText = data.diagnosis;
            resultContainer.classList.remove('hidden');
        } else {
            alert("ত্রুটি: " + data.message);
            if (placeholderResult) placeholderResult.classList.remove('hidden');
        }
    } catch (error) {
        console.error("Error:", error);
        alert("সার্ভারের সাথে যোগাযোগ করা যাচ্ছে না। আপনার ব্যাকএন্ড কি চালু আছে?");
        if (placeholderResult) placeholderResult.classList.remove('hidden');
    } finally {
        // 5. Reset UI State
        loader.classList.add('hidden');
        btnText.disabled = false;
        btnText.innerText = "রোগ নির্ণয় করুন";
    }
}

// Image Preview Logic
const imageInput = document.getElementById('imageInput');
if (imageInput) {
    imageInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        const previewContainer = document.getElementById('imagePreviewContainer');
        const previewImage = document.getElementById('imagePreview');

        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                previewImage.src = e.target.result;
                previewContainer.classList.remove('hidden');
            }
            reader.readAsDataURL(file);
        } else {
            previewContainer.classList.add('hidden');
            previewImage.src = "";
        }
    });
}

function clearImage() {
    const imageInput = document.getElementById('imageInput');
    const previewContainer = document.getElementById('imagePreviewContainer');
    const previewImage = document.getElementById('imagePreview');

    if (imageInput) imageInput.value = "";
    if (previewContainer) previewContainer.classList.add('hidden');
    if (previewImage) previewImage.src = "";
}