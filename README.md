# Text Generation API using LFM2.5-350M

## Thông tin sinh viên

* Họ và tên: **Bùi Đặng Khả Tuân**
* MSSV: **24120236**
* Môn học: **Tư duy tính toán**

---

## Mô hình sử dụng

* Tên mô hình: **LFM2.5-350M**
* Nguồn: Hugging Face
* Link: https://huggingface.co/LiquidAI/LFM2.5-350M

---

## Mô tả hệ thống

Hệ thống xây dựng một Web API sử dụng FastAPI nhằm khai thác mô hình ngôn ngữ (Language Model) từ Hugging Face.

API cho phép người dùng nhập vào một đoạn văn bản (prompt), sau đó hệ thống sẽ sử dụng mô hình để sinh ra văn bản tiếp theo (text generation).

---

## Cài đặt thư viện

### Bước 1: Tạo môi trường

```bash
python -m venv venv
```

### Bước 2: Kích hoạt môi trường

```bash
venv\Scripts\activate
```

### Bước 3: Cài thư viện

```bash
pip install -r requirements.txt
```

---

## Hướng dẫn chạy chương trình

Chạy server bằng lệnh:

```bash
uvicorn main:app --reload
```

Sau khi chạy thành công, truy cập:

```text
http://127.0.0.1:8000/docs
```

để sử dụng giao diện Swagger UI.

---

## Hướng dẫn gọi API

### 1. API kiểm tra hệ thống

```http
GET /
```

**Response:**

```json
{
  "message": "Text Generation API"
}
```

---

### 2. API kiểm tra trạng thái

```http
GET /health
```

**Response:**

```json
{
  "status": "ok"
}
```

---

### 3. API sinh văn bản

```http
POST /generate
```

**Request:**

```json
{
  "prompt": "AI will change the world because"
}
```

**Response:**

```json
{
  "input": "AI will change the world because",
  "output": "AI will change the world because..."
}
```

---

## Example Output

**Input:**

```json
{
  "prompt": "Explain AI"
}
```

 **Output:**

```json
{
  "input": "Explain AI",
  "output": "Explain AI and its impact on the world..."
}
```
## Cấu trúc project

```bash
Lab_API/
├── main.py
├── test_api.py
├── requirements.txt
└── README.md
```

---


