from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/post")
async def receive_data(request: Request):
    # Obter todos os headers
    headers = dict(request.headers)

    # Obter o content-type
    content_type = headers.get("content-type", "unknown")
    auth_header = headers.get("authorization", None)

    # Obter corpo da requisição (em bytes)
    body_bytes = await request.body()
    body_text = body_bytes.decode('utf-8', errors='replace')

    print("\n==== NOVA REQUISIÇÃO RECEBIDA ====")
    print(f"📄 Content-Type: {content_type}")
    if auth_header:
        print(f"🔐 Authorization: {auth_header}")
    print("🧾 Headers completos:")
    for k, v in headers.items():
        print(f"   {k}: {v}")
    print("📦 Corpo da requisição:")
    print(body_text)
    print("==================================\n")

    return {
        "message": "Dados recebidos com sucesso",
        "content_type": content_type,
        "auth": auth_header,
        "headers": headers,
        "raw_body": body_text
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
