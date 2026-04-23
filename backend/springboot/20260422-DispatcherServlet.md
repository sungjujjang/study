# DispatcherServlet
** HTTP 프로토콜로 들어오는 모든 요청을 제일 먼저 받아 적합한 컨트롤러에 위임하는 프론트 컨트롤러**
![디스패치 서블릿의 구조](https://blog.kakaocdn.net/dna/bcff5H/btstbdRuSr9/AAAAAAAAAAAAAAAAAAAAAMAxIBGus8UUBRtjJl5FHhYPV733Ng6534bpVp1FfBj5/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1777561199&allow_ip=&allow_referer=&signature=1bLOO%2BNPXnqZLc%2FpHFxT8sX6bnI%3D)

## HandlerMapping
DispatcherServlet이 처리해야 할 컨트롤러를 식별하는 방식

## 스프링 MVC 패턴
![스프링 MVC 패턴](https://media.vlpt.us/images/miscaminos/post/80555c98-2846-4774-9b27-9746336f3dce/springMVC_Dispatcher_centered.jpg)
위와 같이 전달 - 전달 - 전달해주는 구조를 스프링이 사용하는 MVC 패턴이라고 한다
