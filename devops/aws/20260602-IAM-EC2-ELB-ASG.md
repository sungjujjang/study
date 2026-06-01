# IAM
- 사용자 생성 및 그룹에 배치
- ROLE 부여 가능해 서비스에 안전 접근 허용
# EC2
- 클라우드 가상 서버(VPS)
- security group을 통해 보안 그룹 제어
- 예측 가능한 요금 범위
- SPOT INSTANCE 를 통해 최대 90%의 요금을 절약 가능
	- 하지만 언제나 종료될 수 있음
# Elastic Load Balancer
- 부하를 다수의 인스턴스로 분산하는 서비스
- 여러 인스턴스의 단일 엑세스 지점(EndPoint)을 지정
- 고가용성을 보장하기 위해 health-check 수행
- http, tcp, websocket 등 여러 프로토콜 사용 가능
```
USER <--HTTPS--> LB <--HTTP--> EC2
```
# Auto Scaling Group
- 부하 증가시 인스턴스 추가
- 부하 감소시 인스턴스 삭제
- 모두 자동화하는 서비스
- 주로 EC2 인스턴스를 다룰 수 잇슴
