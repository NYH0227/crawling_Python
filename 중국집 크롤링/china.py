### 부평구 중국집 10개의 이름, 주소, 별점, 리뷰를 별점순으로 정렬해서 출력 ###

from selenium import webdriver
import time

# 데이터가 있는 iframe에서의 처리
def go2TargetIframe(driver):
    # entryIframe로 들어감
    driver.switch_to.frame(driver.find_element_by_id("entryIframe"))

    # 동적으로 생기는 리뷰를 찾기위해
    # 마우스 초점을 iframe안으로 이동시킨 후 두번 아래로 스크롤
    driver.find_element_by_xpath('//*[@id="app-root"]/div/div/div[2]/div[1]/div[2]').click()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 현재 iframe에서 이름,주소,별점,리뷰(3개)를 반환받아 data에 삽입
    data.append(getData(driver))

    # entryIframe에서 탈출
    driver.switch_to.default_content()
    #time.sleep(1)


# 데이터 삽입
def getData(driver):
    review = []
    name = driver.find_element_by_class_name('_3XamX').text
    addr = driver.find_element_by_class_name('_2yqUQ').text
    try: 
        grade = driver.find_element_by_xpath('//*[@id="app-root"]/div/div/div[2]/div[1]/div[1]/div[2]/span[1]/em').text
    except : 
        grade = 0.0
    r = driver.find_elements_by_class_name('WoYOw')
    for i in r:
        review.append(i.text.strip())
    if len(r) == 0: 
        review.append("리뷰가 아직 없습니다.")

    return [name,addr,float(grade),review]


# main
url = 'https://map.naver.com/v5/search/%EB%B6%80%ED%8F%89%EA%B5%AC%EC%A4%91%EA%B5%AD%EC%A7%91?c=14102884.1476490,4510021.5456387,12,0,0,0,dh'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

data = []
num = 10

for i in range(1,num+1):
    # 중국집 목록이 있는 iframe으로 들어감
    driver.switch_to.frame(driver.find_element_by_id("searchIframe"))

    # i번째 음식집의 데이터가 있는 Iframe이 생기도록 클릭함
    driver.find_element_by_xpath('//*[@id="_pcmap_list_scroll_container"]/ul/li['+str(i)+']/div[1]/a/div[1]/div/span').click()
    time.sleep(1)
    # entryIframe으로 가기 위해 searchIframe에서 탈출
    driver.switch_to.default_content()
    go2TargetIframe(driver)

data = sorted(data, key=lambda x : x[2],reverse=True)
for i in data:
    print(*i)
    print()

time.sleep(2)
driver.quit()
