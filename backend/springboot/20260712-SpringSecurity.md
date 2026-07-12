# 스프링 시큐리티
- 요청이 컨트롤러에 도달하기 전에 가로채 서블릿 필터 체인 위에서 인증/인가를 수행하는 라이브러리

## 동작 순서
1. DelegatingFilterProxy
	- 서블릿 컨테이너와 스프링 컨텍스트들을 연결함
2. FilterChainProxy
	- 실제 보안 로직이 담긴 SecurityFilterChain을 관리, 순차 실행시킴
3. 인증 필터
	- 사용자가 정의한 인증 필터 로직이 실행됨
4. ExceptionTranslationFilter
	- 인증/인가 예외를 반환함
5. AuthorizationFilter
	- hasRole(), @PreAuthorize 등으로 Role 검사 수행

## Role 설정 방법
- SecurityFilterChain에서 URL 기반 설정
```
	http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .requestMatchers("/api/user/**").hasAnyRole("USER", "ADMIN")
                .requestMatchers("/api/public/**").permitAll()
                .anyRequest().authenticated()
            )
```

