import requests

# Địa chỉ server (nhớ đúng port 8005)
url = "http://127.0.0.1:8005/ask"

# Câu hỏi bạn muốn hỏi

while True:
    my_question = input()  # Thay đổi câu hỏi ở đây

    try:
        print(f"Đang gửi câu hỏi: {my_question} ...")
        response = requests.post(url, json={"question": my_question})
        
        # In kết quả
        if response.status_code == 200:
            print("--- TRẢ LỜI TỪ AI ---")
            print(response.json()['answer'])
        else:
            print("Lỗi:", response.text)
            
    except Exception as e:
        print(f"Không kết nối được server: {e}")