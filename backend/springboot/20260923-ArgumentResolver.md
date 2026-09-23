# ArgumentResolver 
- 중복된 코드를 처리하기 위한 인터페이스
- ArgumentResolver가 실행되길 원하는 Parameter의 앞에 특정 어노테이션을 생성해 붙이면 공통 로직인 ArgumentResolver가 실행된다.

## HandlerMethodArgumentResolver
- ArgumentResolver의 구현체로, 아래 두 메서드를 구현해야 한다.
```java
boolean supportsParameter(MethodParameter parameter)

@Nullable
Object resolveArgument(MethodParameter parameter, @Nullable ModelAndViewContainer mavContainer, NativeWebRequest webRequest, @Nullable WebDataBinderFactory binderFactory)
```
- supportsParameter
  - 요청받은 메서드의 인자에 특정 어노테이션이 붙어있는지 확인하고, 붙어있으면 true를 반환한다.
- resolveArgument
  - 실제 공통 로직이 들어가는 부분이다.

## WebConfig
```java
@RequiredArgsConstructor
@Configuration
public class WebConfig implements WebMvcConfigurer {
    private final LoginUserArgumentResolver loginUserArgumentResolver;

    @Override
    public void addArgumentResolvers(List<HandlerMethodArgumentResolver> argumentResolvers) {
        argumentResolvers.add(loginUserArgumentResolver);
    }
}
```
- 구현이 끝난 어노테이션(ArgumentResolver)은 WebConfig에 등록에 스프링에게 알려주어야 한다.

## 요청 처리 순서
- 사용자가 웹 브라우저를 통해 요청하면 DispatcherServlet이 이를 받음
- DispatcherServlet은 해당 요청에 맞는 URI를 HandlerMapping에서 검색
    - 이 때, RequestMapping으로 구현한 API를 찾게 되는데, 이들은 RequestMappingHandlerAdapter가 모두 가지고 있음.
    - 원하는 Mapping을 찾은 경우, 첫 번째로 Intercepter를 처리
    - Argument Resolver 처리
    - Message Converter 처리
- Controller Method Invoke