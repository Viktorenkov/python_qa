#task_1_створити АРІ на базі гугл таблиці, містить поля "назва товару", "опис товару", "ціна" (інтова чи флоат), 
#"залишок" (інтовий чи флоат), "містить глютен" (булеве тру чи фолс (виставляєте прапорцем). заповнити мінімум 10 позицій. 
#дані мають бути отримати по зовнішньому ключу "goods" (not "data")

#table_of_goods
#https://docs.google.com/spreadsheets/d/10IwMC1NOmxflfPwlzdv7cxV07mMXbUTzu2sxtl6LL2k/edit?usp=share_link
#json url
#https://script.googleusercontent.com/macros/echo?user_content_key=BnNVjCpPhZ4YNeWWbDknC3HxvgKOmAAo8h1N1gtEi3s9EGpCCFERzrffD8mYM4PsvcBbVdBPKAOfmMWlsJYSUlVYx7JyIuIQm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnK5zQBDYXl_mOYuXyF-VGZwsRZC82cQjklNZEu9_4Qs7QvIZ4BxQ_UowCgNBYqkFcdSKJN26chW0Yt3M7F61M_1iTFGgMiFE3tz9Jw9Md8uu&lib=MoPXG4wonAChj-B1OziooWc2_kmfSSr-t

#task_2_за допомогою requests завантажити створені дані. порахувати вартість всіх товарів та товарів без глютена.

from pprint import pprint
import requests

url = 'https://script.googleusercontent.com/macros/echo?user_content_key=-wMwMsjKPK7BJTS8n0Nz7gYsMPo-GoNt9BfT0y6z74OxV2QdFmLkBVzca-qbnGpPdUOh8Rz8_lVGI4u_i3kwM2joOYsczjyUm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnGyHnlzZxFozotJsdfVuI4IaP-clb2BOlXhHBUak6DbflgJXRBHfWUEW7hwXYgni91Mg831PqqoYP-fm8inByanU_2KHlqvWWtz9Jw9Md8uu&lib=MoPXG4wonAChj-B1OziooWc2_kmfSSr-t'

response = requests.get(url)
goods = response.json()

goods_total_cost = 0
gluten_free_goods_cost = 0

for item in goods['goods']:
    goods_total_cost += float(item['priсe'])
    if item['gluten_y/n']:
        gluten_free_goods_cost += float(item['priсe'])

print("Вартість всіх товарів: ", goods_total_cost)
print("Вартість товарів без глютену: ", gluten_free_goods_cost)




