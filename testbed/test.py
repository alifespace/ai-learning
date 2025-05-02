import requests
import time

def count_tokens(text):
    # 简单 token 估算方式：按空格分词
    return len(text.split())

prompt = "python 中闭包的特点?"
start_time = time.time()

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "qwen3:4b",
    "prompt": prompt,
    "stream": False  # 一定设为 False，否则不好统计
})

end_time = time.time()
elapsed = end_time - start_time

data = response.json()
generated_text = data['response']
token_count = count_tokens(generated_text)

print(f"Output: {generated_text}")
print(f"Tokens generated: {token_count}")
print(f"Time elapsed: {elapsed:.2f} seconds")
print(f"Tokens per second (TPS): {token_count / elapsed:.2f}")
