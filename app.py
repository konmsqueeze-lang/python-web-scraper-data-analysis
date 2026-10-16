import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "http://books.toscrape.com/"
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
soup = BeautifulSoup(resp.text, "html.parser")

book_list = []
books = soup.find_all("article", class_="product_pod")

for book in books:
    a_tag = book.find("a")
    title = a_tag.get("title", "")
    price = book.find("p", class_="price_color").get_text(strip=True)
    book_list.append({"书名": title, "价格": price})

df = pd.DataFrame(book_list)
df.to_csv("书籍数据.csv", index=False, encoding="utf-8-sig")
print(f"成功抓取{len(book_list)}条数据，已保存为书籍数据.csv")

if len(df) > 0:
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    price_count = df["价格"].value_counts().head(5)
    price_count.plot(kind="bar")
    plt.title("书籍价格分布")
    plt.show()
