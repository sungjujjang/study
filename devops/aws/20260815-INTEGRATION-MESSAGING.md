# Integration & Messaging

SQS: 대기열 모델 사용

SNS: Pub/Sub 모델

Kinesis: 실시간 스트리밍 / 대용량 데이터


# Amazon SQS

Producer → SQS Queue ← Consumer
Producer → SQS Queue ← Consumer
Producer → SQS Queue ← Consumer

Send → SQS Queue ← Poll

구체적 처리 가능 / 최대 보존 14일 / 최대 256 KB msg

지연 시간이 10ms 내외

큐 대기 사용해서 ASG 정책 지정 가능

Consumer가 메시지 풀링 → 다른 소비자에게 안 보여짐
(Delete 하지 않을시 최대 30초 = 가시성 제한 시간)

초당 300개, 배치 처리시 초당 3000개 처리 OK


# Amazon SNS

Kafka와 비슷한 서비스 (메시지 보관 X)

서버가 메시지를 특정 topic으로 전송 가능하다.

→ topic을 구독한 서버가 받는다.

topic 최대 1250만개 구독 가능

topic은 최대 10만개 생성 가능

AWS에 있는 서비스들이 수신 가능하다 (직접)


# SNS + SQS 통합해 사용

예) 방송국 → 우편함


# Kafka VS SNS + SQS

Kafka
→ 이벤트 기록

SNS + SQS
→ 처리 작업


# AWS Kinesis

Kafka와 비슷하지만 AWS 서비스 중심


# AWS MQ

RabbitMQ / ActiveMQ를 위한 AWS 관리형 서비스

Multi-AZ를 지원 복구 기능