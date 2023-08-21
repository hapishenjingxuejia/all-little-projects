import requests
import easygui

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.exceptions.RequestException as e:
        print("error:", e)
        return None

# 爬取谷歌首页的 HTML 内容
url = "https://www.google.com"
html = get_html(url)

if html:
   easygui.codebox("hello", "sys", html)
