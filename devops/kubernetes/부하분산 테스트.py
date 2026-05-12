import requests
import re
from collections import Counter

# 대상 URL
url = "http://34.66.5.220:30082/"
ip_counts = Counter()

# IP 패턴: 10.으로 시작하고 숫자.숫자.숫자:포트번호 형태
# \d+는 숫자가 1개 이상 반복됨을 의미합니다.
ip_pattern = r"10\.\d+\.\d+\.\d+:\d+"

print(f"{url}에서 10.*.*.*:* 패턴 추출 중 (총 100회)...")

for i in range(1, 101):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            # 텍스트 전체에서 해당 패턴을 모두 찾음
            found_ips = re.findall(ip_pattern, response.text)
            
            if found_ips:
                # 첫 번째로 매칭된 IP 주소를 가져옴
                server_ip = found_ips[0]
                print(f"{i}회: 추출된 IP - {server_ip}")
                ip_counts[server_ip] += 1
            else:
                ip_counts["패턴 매칭 실패"] += 1
        else:
            ip_counts[f"HTTP 에러({response.status_code})"] += 1
            
    except Exception as e:
        ip_counts[f"접속 에러({type(e).__name__})"] += 1
    
    if i % 20 == 0:
        print(f"{i}회 시도 완료...")

# 결과 출력
print("\n" + "="*40)
print(f"{'추출된 내부 IP (10.x.x.x:port)':<30} | {'횟수'}")
print("-"*40)

for ip, count in ip_counts.most_common():
    print(f"{ip:<34} | {count}회")

print("="*40)