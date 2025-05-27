# Style Transfer API

This is a **simple API** I'm building to learn more about **AI and machine learning**, specifically how to apply artistic style transfer to images. It uses a pre-trained TensorFlow Hub model to transform photos with the style of classic works by artists like Van Gogh, Picasso, and others.

---

## 🚀 Features

* **Arbitrary style transfer** between two images (content and style).
* Built with **TensorFlow Hub** and **FastAPI** for performance and scalability.
* **Easy integration** via HTTP requests with JPEG/PNG image formats.
* Great for generative art projects, creative editing, and learning about computer vision.

---

## 🛠️ Technologies

* Python 3.10+
* FastAPI
* TensorFlow 2.x
* TensorFlow Hub
* Pillow (PIL)
* Uvicorn (ASGI server)

---

## ⚙️ Usage

### Clone the Repository

```bash
git clone [https://github.com/DairaDoo/Style-Transfer-API.git](https://github.com/DairaDoo/Style-Transfer-API.git)
cd Style-Transfer-API
Create a Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt


### Run the Server

```bash
uvicorn app.main:app --reload
Access the Interactive Documentation
Open your browser to:

Bash

http://localhost:8000/docs
📝 API Endpoint
POST /style-transfer

Parameters:

content_image: Image file for the content (your photo).
style_image: Image file for the style (a painting or artistic image).
Response: A JPEG image with the applied style transfer.

📸 Example Usage
You can test this with tools like Postman or cURL by sending a POST request with two images (content_image and style_image). You'll receive the transformed image in the response.

📦 Suggested requirements.txt
Plaintext

fastapi
uvicorn
tensorflow
tensorflow-hub
pillow

📝 License
This project is under the MIT License. See the LICENSE file for more information.

🤝 Contributions
Contributions are welcome! Feel free to open issues or pull requests for suggestions, improvements, or bug fixes.

📫 Contact
Dairan S. De Jesús Mora
Puerto Rico
GitHub: DairaDoo