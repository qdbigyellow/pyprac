from fake_useragent import UserAgent # 随机产生header，这样在爬取的过程中就不会被认为是从同一个地方来的。 通过随意变换headers，一定要有随机性，非常方便
import requests
import pandas as pd
from bs4 import BeautifulSoup # 用于html的解析, 看文档学习用法

class LianJiaSpider(object):
    def __init__(self):
        self.ua = UserAgent()
        self.headers = {"User-Agent": self.ua.random}
        self.data = list()

    def get_max_page(self, url):
        """获取当前页面的最大页数"""        
        response = requests.get(url, headers=self.headers)            
        if response.status_code == 200:
            source = response.text
            soup = BeautifulSoup(source, 'html.parser')
            a = soup.find_all("div", class_="page-box house-lst-page-box")
            max_page = eval(a[0].attrs["page-data"])["totalPage"]
            return max_page
        else:
            print(f"请求失败 statue: {reponse.status_code}")
            return None

    def get_parse_page(self, url):
        max_page = self.get_max_page(url)
        for i in range(1, max_page + 1):
            url = f'https://sh.lianjia.com/zufang/pa{i}/'
            print("当前正在爬取: {}".format(url))
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            a = soup.find_all("div", class_="info-panel")
            for j in range(len(a)):
                try:
                    link = a[j].find("a")["href"]
                    print(link)
                    detail = self.parse_detail(link)
                    self.data.append(detail)
                except:
                    print('get page link is fail')
                    continue
        print("所有数据爬取完成，正在存储到 csv 文件中")
        data = pd.DataFrame(self.data)
        data.to_csv("链家网租房数据.csv", encoding='utf_8_sig')

    def parse_detail(self, url):
        detail = {}
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            b = soup.find("div", class_="content zf-content")
            detail["月租金"] = int(b.find("span", class_="total").text.strip())
            detail["面积"] = b.find_all("p", class_="lf")[0].text[3:].strip()
            detail["房屋户型"] = b.find_all("p", class_="lf")[1].text[5:].strip()
            detail["楼层"] = b.find_all("p", class_="lf")[2].text[3:].strip()
            detail["房屋朝向"] = b.find_all("p", class_="lf")[3].text[5:].strip()
            detail["地铁"] = b.find_all("p")[4].text[3:].strip()
            detail["小区"] = b.find_all("p")[5].text[3:].split('-')[0].strip()
            detail["位置"] = b.find_all("p")[6].text[3:].strip()
            return detail
        else:
            print("请求失败 statue: {}".format(reponse.status_code))
            return None


if __name__ == "__main__":
    s = LianJiaSpider()
    s.get_parse_page('https://sh.lianjia.com/zufang/minhang/')