# Python 网页爬虫与数据可视化项目
## 项目简介
本项目使用Python实现网页书籍数据采集，完成数据清洗、导出表格与可视化统计。
从网页抓取书籍信息，保存到CSV文件，再对数据进行简单分析，绘制图表，完整实现「抓取-存储-分析-可视化」流程。

## 技术栈
- Python
- requests：发送HTTP请求，获取网页源码
- BeautifulSoup4：解析HTML，提取页面书籍信息
- Pandas：数据清洗、表格处理
- Matplotlib：数据可视化绘图

## 环境依赖安装
```bash
pip install requests beautifulsoup4 pandas matplotlib
