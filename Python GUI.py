from tkinter import *
import mysql.connector

# MySQL 연결 설정
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="mydb"
)

cursor = mydb.cursor()

# 데이터베이스에서 카페 정보 가져오기
def cafeTable():
    cursor.execute("SELECT * FROM cafeTable")
    cafe_info = cursor.fetchall()
    return cafe_info

# 데이터베이스에서 카테고리 정보 가져오기
def categoryTable(cafe_id):
    cursor.execute("SELECT * FROM categoryTable WHERE CAFE_ID = %s", (cafe_id,))
    category_info = cursor.fetchall()
    return category_info

# 데이터베이스에서 메뉴 정보 가져오기
def menuTable(cafe_id, category_id):
    cursor.execute("SELECT * FROM menuTable WHERE CAFE_ID = %s AND CATEGORY_ID = %s", (cafe_id, category_id,))
    menu_info = cursor.fetchall()
    return menu_info

# 카페 창 생성
cafe_window = Tk()
cafe_window.title("Cafe")

# 카페 정보 가져오기
cafes = cafeTable()

# 메뉴 버튼 누를 때
def menu_click(mcafe_id, mcategory_id, menu_name):
    print(f"{mcafe_id},{mcategory_id},{menu_name}")

    #모든 창 종료
    cafe_window.destroy()

# 카테고리 버튼 누를 때
def category_click(ccafe_id, category_id):
    # 메뉴 창 생성
    menu_window = Toplevel()
    menu_window.title("Menu")

    # 메뉴 정보 가져오기
    menus = menuTable(ccafe_id, category_id)

    # 메뉴 버튼 생성
    for menu in menus:
        mcafe_id = menu[0]
        mcategory_id = menu[1]
        menu_name = menu[2]
        price = menu[3]
        
        menu_text = menu_name+"     "+ str(price)
        menu_button = Button(menu_window, text=menu_text, command=lambda id=mcafe_id, cid=mcategory_id, mid=menu_name : menu_click(id, cid, mid),width = 50, anchor="w")
        menu_button.pack()
    
    # 창 실행
    menu_window.mainloop()

# 카페 버튼 누를 때
def cafe_click(cafe_id):
    # 카테고리 창 생성
    category_window = Toplevel()
    category_window.title("Category")

    # 카테고리 정보 가져오기
    categories = categoryTable(cafe_id)

    # 카테고리 버튼 생성
    for category in categories:
        ccafe_id = category[0]
        category_id = category[1]
        category_name = category[2]

        category_button = Button(category_window, text=category_name, command=lambda id=ccafe_id, cid=category_id : category_click(id, cid),width = 50, anchor="w")
        category_button.pack()

    # 창 실행
    category_window.mainloop()

# 카페 이름을 가지는 버튼 생성
for cafe in cafes:
    cafe_id = cafe[0]
    cafe_name = cafe[1]
    ADDRESS = cafe[2]

    button_cafe = cafe_name+"   "+ADDRESS
    cafe_button = Button(cafe_window, text=button_cafe, command=lambda id=cafe_id, : cafe_click(id),width = 50, anchor="w")
    cafe_button.pack()

# 창 실행
cafe_window.mainloop()

# MySQL 연결 종료
cursor.close()
mydb.close()

