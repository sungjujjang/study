# EC2 - Associate
- Private vs Public IP
    - private
      - 내부망의 아이피
      - NAT + 인터넷 게이트웨이 통해 외부망과 소통함
    - public
      - WWW상에서 단 한개만 존재하는 식별자 아이피

- EC2 인스턴스는 IP 고정이 없음
  - 고정 아이피가 필요함
  
## Elastic IPS 사용
- 고정 아이피를 연결할 수 있도록 하는 서비스
- 하나의 AWS 계정당 최대 5개 생성 가능하다
- 현재는 쓰지 않고 아래 서비스를 이용한다
  - ELB를 통해 아이피 연결 없이 사용
  - 퍼블릭 아이피 자동 할당을 사용

## 배치 그룹 (Placement Group)
- Cluster
  - 모든 인스턴스가 동일 (하드웨어) 랙에 있음
  - 우수한 네트워크를 자랑함 (10 Gbps)
  - 하나의 랙에 장애시 전체 인스턴스에 장애가 걸림
- Spread
  - 여러 AZ(가용 영역)에 걸쳐서 사용됨
  - 동시 장애 위험이 감소함
  - 배치 그룹당 최대 7개의 인스턴스만 사용 가능
- Partiton
  - 파티션 1개 = 랙 1개
  - 각 AZ당 7개 파티션 가능
  - 최대 100개의 EC2 사용 가능
  - 여러 AZ에 걸쳐서 사용 가능

## Elastic Network Interfaces (ENI)
- 가상의 랜카드
- EC2를 샏성할 떄 자동으로 생성되어 붙여짐
  - 모든 인스턴스는 하나 이상의 ENI를 가지고 있음
- 실질적으로 서브넷을 구축했을 떄 인스턴스가 서브넷 안에 들어가는 것이 아니라 ENI가 들어가게 됨
![서브넷 이미지 1](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FdASx4m%2FbtsDuuJ9xye%2FAAAAAAAAAAAAAAAAAAAAAOb1Wb6jbFucAYpj1427NmPxbukB8kEvaJXHNpWQFK4l%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1785509999%26allow_ip%3D%26allow_referer%3D%26signature%3DZpvBb7ElUeBMKCwfN5Kq4y8bVfs%253D)

## 서브넷이란
- 네트워크 영역을 나누는 것
- VPC를 생성한 이후, IP 대역을 지정해 서브넷 영역을 구축한다
- 프라이빗 서브넷과 퍼블릭 서브넷으로 나뉜다
  - 프라이빗 서브넷
    - 외부 네트워크와 단절된 네트워크 영역
    - 외부 네트워크로 나가려면 NAT Gateway을 사용해야 한다
    - NAT Gateway는 퍼블릭 서브넷에 생성된다
  - 퍼블릭 서브넷
    - 외부 네트워크와 연결되는 서브넷
    - 중요 정보는 여기다가 올리면 안 된다
- VPC는 외부와 통신하기 위해서 인터넷 게이트웨이를 사용한다.
  - 인터넷 게이트웨이도 생성해 주어야 한다.
- 라우팅 테이블
  - 각각의 서브넷은 서로 다른 네트워크 영역이기 때문에 라우팅 테이블을 통해 연결해 주어야 한다.
  - 자동으로 서브넷끼리 통신이 가능하도록 라우팅 테이블이 세팅된다.
  - 정학히는, 내부에서 발생한 트래픽을 어느 방향으로 처리하는지 세팅하는 테이블이다
  - 따라서 인터넷 게이트웨이 또한 내부 아이피를 제외한 모든 아이피이므로, 남은 0.0.0.0/0 전체 아이피들은 인터넷 게이트웨이로 라우팅시키는 과정이 필요하다.