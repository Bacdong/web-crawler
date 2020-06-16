import requests

res = requests.get('https://video.vnexpress.net/tin-tuc/nhip-song/ai-quyet-dinh-may-bay-ha-canh-trong-thoi-tiet-xau-4116382.html#vn_source=Home&vn_campaign=ThuongVien&vn_medium=Item-3&vn_term=Desktop&vn_thumb=0')
print(res.text)