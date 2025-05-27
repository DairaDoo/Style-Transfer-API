# app/main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from style_transfer_api import transfer_style
import io

app = FastAPI(title="Van Gogh Style Transfer API")

@app.post("/style-transfer")
async def style_transfer_endpoint(
    content_image: UploadFile = File(...),
    style_image: UploadFile = File(...)
):
    """
    Recibe dos imágenes (contenido y estilo), aplica Style Transfer y devuelve la imagen resultante.
    """
    content_bytes = await content_image.read()
    style_bytes = await style_image.read()

    result_image = transfer_style(content_bytes, style_bytes)

    # Convertir imagen resultante a flujo de respuesta HTTP
    img_io = io.BytesIO()
    result_image.save(img_io, format='JPEG')
    img_io.seek(0)

    return StreamingResponse(img_io, media_type="image/jpeg")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

