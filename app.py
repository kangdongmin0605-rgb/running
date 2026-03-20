import requests
from bs4 import BeautifulSoup
import time

def get_motivation_quote():
    """온라인에서 오늘의 명언/제목을 가져오는 기능"""
    try:
        # 명언 사이트나 뉴스 헤드라인 등을 가져올 수 있습니다. 
        # 여기서는 간단하게 네이버 뉴스 IT 섹션의 첫 번째 헤드라인을 '오늘의 뉴스'로 가져올게요.
        url = "https://news.naver.com/section/105"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # 첫 번째 뉴스 제목 가져오기
        title = soup.select_one(".sa_text_title").text.strip()
        return title
    except:
        return "포기하지 마세요! 오늘보다 더 나은 내일이 기다립니다."

def start_program():
    print("========================================")
    print("   🏃‍♂️ RUNNING RECOVERY MANAGER v1.0   ")
    print("========================================")
    
    # 1. 온라인 데이터 가져오기 (시연용)
    print("🔍 실시간 데이터 로딩 중...")
    time.sleep(1)
    news_tip = get_motivation_quote()
    print(f"📢 [오늘의 IT 이슈]: {news_tip}")
    print("----------------------------------------")

    # 2. 유저 입력 받기
    try:
        weight = float(input("⚖️ 현재 몸무게(kg)를 입력하세요: "))
        distance = float(input("🛣️ 오늘 달린 거리(km)를 입력하세요: "))
        
        # 3. 칼로리 계산 로직
        # 공식: 몸무게 * 거리 (일반적인 조깅 기준)
        burned_calories = weight * distance
        
        print("\n[📊 분석 결과]")
        print(f"🔥 소모 칼로리: 약 {burned_calories:.0f} kcal")
        
        # 4. 음식 추천 로직
        print("\n[🍲 추천 회복 식단]")
        if distance < 5:
            print("👉 가벼운 운동을 하셨네요! '바나나 1개와 우유 한 잔'을 추천합니다.")
        elif 5 <= distance < 10:
            print("👉 적당한 운동! 근육 회복을 위해 '닭가슴살 샐러드와 삶은 달걀'은 어떨까요?")
        else:
            print("👉 장거리 러닝 대단해요! '소고기 스테이크나 든든한 파스타'로 영양을 보충하세요!")
            
    except ValueError:
        print("❌ 숫자만 입력해 주세요!")

    print("\n========================================")
    print("   오늘도 수고하셨습니다! 내일 또 만나요!   ")
    print("========================================")

if __name__ == "__main__":
    start_program()