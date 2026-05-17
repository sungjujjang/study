# 인그레스(traefik)
- url별 요청 등을 처리하기 위한 것
- user.a.com, auth.a.com 이런 url별 처리 다르게
- SSL/TSL 인증서 등을 한번에 관리
- L7 스위치와 유사한 기능
- nginx가 가장 유명하지만 traefik은 관리자 대시보드를 지원함
- **IgressRoute** 라는 CRD를 활용해 인그레스 설정(CRD : deployment, service 같은 Kind인데 사용자 지정)
- 기본 설정으로 인증서가 있긴 함
```
요청 - LB - IngressRouter - ClusterIP SVC - <pod1, pod2, pod3>(부하분산 됨)
```

