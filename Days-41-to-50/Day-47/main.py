import requests
from bs4 import BeautifulSoup


URL = "https://www.amazon.in/JBL-C100SI-Ear-Headphones-Black/dp/B01DEWVZ2C/ref=sr_1_2?_encoding=UTF8&_ref" \
      "=dlx_gate_sd_dcl_tlt_cb66d3f1_dt&content-id=amzn1.sym.a532052b-26f3-4811-a261-3b35ffa57237&m=A14CZOWI0VEHLG" \
      "&pd_rd_r=9620d2aa-2261-4686-9c97-c3e526eb467a&pd_rd_w=EGp2R&pd_rd_wg=Zpgmg&pf_rd_p=a532052b-26f3-4811-a261" \
      "-3b35ffa57237&pf_rd_r=7NZ754F1MRCNQHCEZD88&refinements=p_6%3AA14CZOWI0VEHLG&sr=8-2"

# enter_url = input("URL: ")

params = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
                        "Chrome/111.0.0.0 Safari/537.36", "Accept-Language": "en-US,en;q=0.8"}

response = requests.get(url=URL, headers=params)

soup = BeautifulSoup(response.text, "html.parser")
my_list =[]

for price in soup.find(class_="priceToPay"):
    my_list += price

item_price = my_list[0]
print(item_price)