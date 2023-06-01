import mysql.connector

# MySQL 연결 설정
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="mydb"
)

cur = mydb.cursor()

# 기존에 있는 테이블 DROP
cur.execute("DROP TABLE IF EXISTS reviewTable");
cur.execute("DROP TABLE IF EXISTS orderTable");
cur.execute("DROP TABLE IF EXISTS memberTable");
cur.execute("DROP TABLE IF EXISTS menuTable");
cur.execute("DROP TABLE IF EXISTS categoryTable");
cur.execute("DROP TABLE IF EXISTS cafeTable");

# TABLE 생성
cur.execute("CREATE TABLE IF NOT EXISTS cafeTable(CAFE_ID INT NOT NULL,CAFE_NAME VARCHAR(50) NOT NULL,ADDRESS VARCHAR(255) NULL,TEL VARCHAR(13) NULL,PRIMARY KEY (CAFE_ID))");
cur.execute("CREATE TABLE IF NOT EXISTS categoryTable(CAFE_ID INT NOT NULL, CATEGORY_ID INT NOT NULL,CATEGORY_NAME VARCHAR(50) NULL,PRIMARY KEY (CAFE_ID, CATEGORY_ID),CONSTRAINT fk_categoryTable_cafeTable FOREIGN KEY (CAFE_ID) REFERENCES cafeTable (CAFE_ID))");
cur.execute("CREATE TABLE IF NOT EXISTS menuTable(CAFE_ID INT NOT NULL, CATEGORY_ID INT NOT NULL, MENU_NAME VARCHAR(50) NOT NULL, PRICE INT NOT NULL, PRIMARY KEY(CAFE_ID, CATEGORY_ID, MENU_NAME), CONSTRAINT `FK_menuTable_categoryTable` FOREIGN KEY(CAFE_ID, CATEGORY_ID) REFERENCES categoryTable(CAFE_ID, CATEGORY_ID),  CONSTRAINT `FK_menuTable_cafeTable` FOREIGN KEY(CAFE_ID) REFERENCES cafeTable(CAFE_ID))");
cur.execute("CREATE TABLE IF NOT EXISTS memberTable(MEMBER_ID INT NOT NULL, MEMBER_NAME VARCHAR(50) NOT NULL, PRIMARY KEY(MEMBER_ID))");
cur.execute("CREATE TABLE IF NOT EXISTS orderTable(ORDER_ID INT NOT NULL, MEMBER_ID INT NOT NULL, CAFE_ID INT NULL, CATEGORY_ID INT NOT NULL, MENU_NAME VARCHAR(50) NULL, DATE DATETIME NULL, QUANTITY INT NULL, PRIMARY KEY(ORDER_ID),CONSTRAINT `FK_orderTable_memberTable` FOREIGN KEY(MEMBER_ID) REFERENCES memberTable(MEMBER_ID), CONSTRAINT `FK_orderTable_menuTable` FOREIGN KEY(CAFE_ID, CATEGORY_ID, MENU_NAME) REFERENCES menuTable(CAFE_ID, CATEGORY_ID, MENU_NAME), CONSTRAINT `FK_orderTable_cafeTable` FOREIGN KEY(CAFE_ID) REFERENCES cafeTable(CAFE_ID))");
cur.execute("CREATE TABLE IF NOT EXISTS reviewTable(REVIEW_ID INT NOT NULL, ORDER_ID INT NULL, SCORE INT NULL, TEXT VARCHAR(255) NULL, DATE DATETIME NULL,PRIMARY KEY(REVIEW_ID), CONSTRAINT `FK_reviewTable_orderTable` FOREIGN KEY(ORDER_ID) REFERENCES orderTable(ORDER_ID))");

# cafeTable에 정보 입력
cur.execute("INSERT INTO cafeTable(CAFE_ID, CAFE_NAME, ADDRESS, TEL) VALUES('011','빽다방','진주대로516번길 6-1','05501101111')");
cur.execute("INSERT INTO cafeTable(CAFE_ID, CAFE_NAME, ADDRESS, TEL) VALUES('012','빽다방','가호동 868-25','05501201212')");
cur.execute("INSERT INTO cafeTable(CAFE_ID, CAFE_NAME, ADDRESS, TEL) VALUES('021','컴포즈','가좌동 858-10번지 KR 일부 1층' ,'05502102121')");
cur.execute("INSERT INTO cafeTable(CAFE_ID, CAFE_NAME, ADDRESS, TEL) VALUES('031','더 벤티','가좌동 1445-7','05503103131')");
cur.execute("INSERT INTO cafeTable(CAFE_ID, CAFE_NAME, ADDRESS, TEL) VALUES('032','더 벤티','가좌동 480-7','05503203232')");
cur.execute("INSERT INTO cafeTable(CAFE_ID, CAFE_NAME, ADDRESS, TEL) VALUES('041','스타벅스','가좌동 1447-9','05504104141')");

# categoryTable에 정보 입력
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('011', '01', 'coffee')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('011', '02', 'beverage')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('011', '03', 'dessert')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('012', '01', 'coffee')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('012', '02', 'beverage')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('012', '03', 'dessert')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('021', '01', 'coffee')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('021', '02', 'beverage')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('021', '03', 'dessert')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('031', '01', 'coffee')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('031', '02', 'beverage')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('031', '03', 'dessert')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('032', '01', 'coffee')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('032', '02', 'beverage')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('032', '03', 'dessert')");
cur.execute("INSERT INTO categoryTable (CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('041', '01', 'coffee')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('041', '02', 'beverage')");
cur.execute("INSERT INTO categoryTable(CAFE_ID, CATEGORY_ID, CATEGORY_NAME) VALUES ('041', '03', 'dessert')");

# menuTable에 정보 입력
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('011', '01', '아메리카노', '1500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('011', '01', '카라멜 마끼야또', '3000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('011', '01', '카페모카', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('011', '01', '콜드브루', '4000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('011', '02', '복숭아 아이스티', '2000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('011', '02', '딸기라떼', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('011', '02', '초코라떼', '3000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('011', '02', '미숫가루', '2500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('011', '02', '쿠키앤크림 프라페', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('012', '01', '아메리카노', '1500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('012', '01', '카라멜 마끼야또', '3000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('012', '01', '카페모카', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('012', '01', '콜드브루', '4000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('012', '02', '복숭아 아이스티', '2000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('012', '02', '딸기라떼', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('012', '02', '초코라떼', '3000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('012', '02', '미숫가루', '2500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('012', '02', '쿠키앤크림 프라페', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('021', '01', '아메리카노', '1500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('021', '01', '카페라떼', '2700')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('021', '01', '카라멜 마끼야또', '3300')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('021', '01', '카페모카', '3300')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('021', '02', '복숭아 아이스티', '3000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('021', '02', '딸기라떼', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('021', '02', '초코라떼', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('021', '02', '쿠키앤크림 프라페', '3900')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('021', '02', '자바칩 프라페', '3900')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('021', '03', '쿠키', '1000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('021', '03', '케잌', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '01', '아메리카노', '2300')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '01', '카페라떼', '3200')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '01', '카라멜 마끼야또', '4000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '01', '카페모카', '4000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '01', '콜드브루', '3800')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '02', '복숭아 아이스티', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '02', '딸기라떼', '4000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '02', '초코라떼', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '02', '미숫가루', '3000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '02', '쿠키앤크림 프라페', '4400')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '02', '자바칩 프라페', '4400')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '03', '쿠키', '2000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('031', '03', '케잌', '5300')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '01', '아메리카노', '2300')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '01', '카페라떼', '3200')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '01', '카라멜 마끼야또', '4000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '01', '카페모카', '4000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '01', '콜드브루', '3800')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '02', '복숭아 아이스티', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '02', '딸기라떼', '4000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '02', '초코라떼', '3500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '02', '미숫가루', '3000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '02', '쿠키앤크림 프라페', '4400')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '02', '자바칩 프라페', '4400')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '03', '쿠키', '2000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('032', '03', '케잌', '5300')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('041', '01', '아메리카노', '4500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('041', '01', '카페라떼', '5000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('041', '01', '카라멜 마끼야또', '5900')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('041', '01', '카페모카', '5500')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('041', '01', '콜드브루', '4900')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('041', '02', '쿠키앤크림 프라페', '6000')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('041', '02', '자바칩 프라페', '6300')");
cur.execute("INSERT INTO menuTable (CAFE_ID, CATEGORY_ID, MENU_NAME, PRICE) VALUES ('041', '03', '케잌', '6900')");

# memberTable에 정보 입력
cur.execute("INSERT INTO memberTable (MEMBER_ID, MEMBER_NAME) VALUES ('01', '이지훈')");
cur.execute("INSERT INTO memberTable (MEMBER_ID, MEMBER_NAME) VALUES ('02', '오은수')");
cur.execute("INSERT INTO memberTable (MEMBER_ID, MEMBER_NAME) VALUES ('03', '왕동기')");
cur.execute("INSERT INTO memberTable (MEMBER_ID, MEMBER_NAME) VALUES ('04', '박진우')");
cur.execute("INSERT INTO memberTable (MEMBER_ID, MEMBER_NAME) VALUES ('05', '이태환')");
cur.execute("INSERT INTO memberTable (MEMBER_ID, MEMBER_NAME) VALUES ('06', '박찬호')");
cur.execute("INSERT INTO memberTable (MEMBER_ID, MEMBER_NAME) VALUES ('07', '김세훈')");
cur.execute("INSERT INTO memberTable (MEMBER_ID, MEMBER_NAME) VALUES ('08', '이진호')");


#제약조건 무력화
cur.execute("SET FOREIGN_KEY_CHECKS =0"); 

# orderTable에 정보 입력
cur.execute("INSERT INTO orderTable(ORDER_ID, MEMBER_ID, CAFE_ID, CATEGORY_ID, MENU_NAME, DATE, QUANTITY) VALUES ('01', '03', '011', '01', '아메리카노', '2023-05-30',  '1')");
cur.execute("INSERT INTO orderTable(ORDER_ID, MEMBER_ID, CAFE_ID, CATEGORY_ID, MENU_NAME, DATE, QUANTITY) VALUES ('02', '08', '041', '02', '자바칩 프라페', '2023-05-30',  '2')");
cur.execute("INSERT INTO orderTable(ORDER_ID, MEMBER_ID, CAFE_ID, CATEGORY_ID, MENU_NAME, DATE, QUANTITY) VALUES ('03',  '06', '021', '03', '케이크', '2023-05-30',  '1')");
cur.execute("INSERT INTO orderTable(ORDER_ID, MEMBER_ID, CAFE_ID, CATEGORY_ID, MENU_NAME, DATE, QUANTITY) VALUES ('04', '02', '011', '01', '콜드브루', '2023-05-30',  '2')");
cur.execute("INSERT INTO orderTable(ORDER_ID, MEMBER_ID, CAFE_ID, CATEGORY_ID, MENU_NAME, DATE, QUANTITY) VALUES ('05',  '07', '031', '02', '미숫가루', '2023-05-30',  '1')");
cur.execute("INSERT INTO orderTable(ORDER_ID, MEMBER_ID, CAFE_ID, CATEGORY_ID, MENU_NAME, DATE, QUANTITY) VALUES ('06', '01', '041', '02', '초코라떼', '2023-05-30',  '2')");
cur.execute("INSERT INTO orderTable(ORDER_ID, MEMBER_ID, CAFE_ID, CATEGORY_ID, MENU_NAME, DATE, QUANTITY) VALUES ('07', '05', '032', '01', '카페모카', '2023-05-30',  '1')");
cur.execute("INSERT INTO orderTable(ORDER_ID, MEMBER_ID, CAFE_ID, CATEGORY_ID, MENU_NAME, DATE, QUANTITY) VALUES ('08', '04', '011', '02', '아이스티', '2023-05-30',  '2')");
cur.execute("INSERT INTO orderTable(ORDER_ID, MEMBER_ID, CAFE_ID, CATEGORY_ID, MENU_NAME, DATE, QUANTITY) VALUES ('09', '01', '021', '01', '카라멜 마끼야또', '2023-5-30', '2')");
cur.execute("INSERT INTO orderTable(ORDER_ID, MEMBER_ID, CAFE_ID, CATEGORY_ID, MENU_NAME, DATE, QUANTITY) VALUES ('10', '08', '012', '03', '쿠키', '2023-05-30',  '1')");

#제약조건 활성화
cur.execute("SET FOREIGN_KEY_CHECKS =1");

# reviewTable에 정보 입력
cur.execute("INSERT INTO reviewTable(REVIEW_ID, ORDER_ID, SCORE, TEXT, DATE) VALUES ('1', '1', '4', '분위기가 아늑하고 조용한 카페입니다.', '2023-06-01')");
cur.execute("INSERT INTO reviewTable(REVIEW_ID, ORDER_ID, SCORE, TEXT, DATE) VALUES ('2', '2', 4, '조용한 시간을 보내기에 안성맞춤입니다.', '2023-06-01')");
cur.execute("INSERT INTO reviewTable(REVIEW_ID, ORDER_ID, SCORE, TEXT, DATE) VALUES (3, 3, 3, ' 벽면의 그림과 조명이 잘 어울려 사진을 찍기에도 좋은 곳입니다.', '2023-06-01')");
cur.execute("INSERT INTO reviewTable(REVIEW_ID, ORDER_ID, SCORE, TEXT, DATE) VALUES (4, 5, 5, '낭만적인 시간을 보내기에 완벽한 장소입니다.', '2023-06-01')");
cur.execute("INSERT INTO reviewTable(REVIEW_ID, ORDER_ID, SCORE, TEXT, DATE) VALUES (5, 6, 3, '조용하고 편안한 분위기에서 시간을 보내기에 좋습니다.', '2023-06-01')");
cur.execute("INSERT INTO reviewTable(REVIEW_ID, ORDER_ID, SCORE, TEXT, DATE) VALUES (6, 8, 4, '아늑하고 포근한 분위기가 특징인 카페입니다. ', '2023-06-01')");
cur.execute("INSERT INTO reviewTable(REVIEW_ID, ORDER_ID, SCORE, TEXT, DATE) VALUES (7, 9, 4, '분위기가 좋아서 휴식하기 좋아요', '2023-06-01')");

mydb.commit()