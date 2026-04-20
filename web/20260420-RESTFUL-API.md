# RESTful API
네트워크 아키텍쳐 원칙을 준수하는 API

## 핵심 6가지 원칙
- CLient-Server
  - 서버(자원을 가진 곳)와 클라이언트(자원을 요청하는 곳)을 명확히 분리한다
- Stateless
  - 서버는 클라이언트의 context를 저장하지 않는다
  - 모든 요청은 독립적으로 이루어져야
- Cahceable
  - 캐싱 기능을 추가하여 응답 속도를 올림
- Uniform Interface
  - 일관된 인터페이스
  - URI로 자원 식별
  - HTTP 메서드로 행위 정의
  - 메시지만 보고도 무엇을 원하는지 알 수 이써야 함
  - 응답에 다음 단계로 갈 수 있는 링크를 포함해야 함
- Layer System
  - 클라이언트는 서버에 대해서 알 수 없어야 함
  - 방화벽을 거치는지 등
- Code on Demand (선택)
  - 서버에서 JS 코드를 보내 클라이언트 기능을 확인할 수 있다

**안 좋은 예** `POST /get_user_info/123`
**좋은 예** `GET /users/123`
URL은 명사로 자원 표현, 행위는 HTTP Method로

