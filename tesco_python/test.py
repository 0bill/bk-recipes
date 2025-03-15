from tesco import get_home_page, get_search_results
import re

request = get_home_page()

match = re.search(r'"csrfToken":"([^"]+)"', request.text)
csrf_token = match.group(1) if match else None

match = re.search(r'_csrf=([^;]+)', request.headers['Set-Cookie'])
csrf_cookie = match.group(1) if match else None

request = get_search_results("Lowicz", csrf_token, csrf_cookie)

print(request.text)