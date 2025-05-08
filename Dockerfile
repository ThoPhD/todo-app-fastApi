# Sử dụng image Python chính thức
FROM python:3.9-slim

# Cài đặt các thư viện cần thiết
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn vào container
COPY . .

# Mở port cho FastAPI (cổng 8000)
EXPOSE 8000

# Chạy FastAPI với uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
