# HTTP
OSI 7계층 중 어플리케이션 계층에 위치
비상태성(StateLess), 비연결성(ConnectioniLess)
- StateLess
  - 서버가 클라이언트의 상태를 보존하지 않음
  - 이를 해결하기 위해 세션, JWT와 같은 개념이 도입
- ConnectionLess
  - 응답 후 연결을 끊얼 자원을 아끼려 함
  - 현대에는 성능을 위해 keep-alive를 사용해 TCP 커넥션을 유지하기도 함

## HTTP Method
- GET
  - 리소스 조회
  - URL에 파라미터가 전체 노출
  - 캐싱이 가능해 정적 리소스에 최적화
- POST
  - 리소스 생성 및 데이터 처리
- PUT
  - 리소스의 전체 교체
  - 요청 페이로드에 리소스의 전체를 담아야 함
- PATCH
  - 리소스의 부분 수정
- DELETE
  - 특정 리소스 삭제
- OPTIONS
  - 리소스의 통신 옵션 확인
  - CORS 요청에 사용됨
- HEAD
  - GET과 동일하지만 바디를 반환하지 않고 헤더 부분만 반환
  - 유효성 검사 등에 사용

## HTTP Packet
http 패킷은 주로 세 부분으로 나뉜다
- Start Line
  - 요청
    - Method + Path + HTTP Version
  - 응답
    - HTTP Version + Status Code + Reason Phrase
- Headers
  - Key: Value 형태
  - 브라우저 정보(User-Agent), Cookie, 인증(Authorization) 정보 등을 포함
- Body
  - 실제 전송할 데이터가 담긴다
  - JSON, XML, HTML, Image 등

## HTTPS
HTTP 아래에 TLS 계층을 추가하여 데이터의 무결성, 기밀성, 가용성을 보장한 프로토콜
**TLS handshake**
1. Client Hello
  - 클라이언트에서 서버에 요청
  - 클라이언트 TLS 버전, 암호화 방식 리스트, 무작위 난수
2. Server Hello
  - 서버가 선택한 암호화 방식
  - 서버가 생성한 무작위 난수
  - 서버의 인증서
3. 인증서 확인
  - 클라이언트 브라우저에 내작된 CA 공개키를 이용해 서버 인증서를 검증
4. Pre Master Secret 생성
  - 클라이언트는 서버 인증서 안의 서버 공개키를 사용해 무작위 데이터를 생성해 보낸다.
5. Master Secret 도출
  - 서버와 클라이언트는 각자 가진 아래 요소를 통해 동일한 대칭 키를 만들어낸다
  - 클라이언트 난수 + 서버 난수 + Pre Master Secret(클라이언트에서 공개 키를 통해 생성한 무작위 데이터)
6. 완료
  - 서로 확인 메시지를 주고받음
  - 이후 모든 데이터는 방금 만들어 낸 대칭 키를 통해 암호화하여 통신

**CA(Certificate Authority)란?**
브라우저(구글 크롬, 파이어폭스, 사파리 등)가 관리하는 인증서
