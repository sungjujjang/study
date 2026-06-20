# K3s + cloudflare tunnel 환경 구성하기

## k3s 설치
```bash
curl -sfL https://get.k3s.io | sh -
```
- traefik ingress 기본 설치(포함)

### kubeconfig 불러오지 못할 때
```bash
mkdir -p ~/.kube

sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config

sudo chown $USER:$USER ~/.kube/config

export KUBECONFIG=$HOME/.kube/config
```

## Cloudflare Cli 설치
```bash
# Debian/Ubuntu
curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared.deb

# RHEL/CentOS
curl -L --output cloudflared.rpm https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-x86_64.rpm
sudo rpm -i cloudflared.rpm
```

## Cloudflare Tunnel 설치
- 로그인
```bash
cloudflared tunnel login
```
- 터널 생성
```bash
cloudflared tunnel create (터널 이름)
```
    - 뒤에 나오는 **/Users/dale/.cloudflared/a1b2c3d4-5678-90ab-cdef-1234567890ab.json** 등의 파일을 메모할 것
    

## Secret 생성
```bash
kubectl create namespace cloudflare

kubectl create secret generic cloudflare-tunnel \
  -n cloudflare \
  --from-file=credentials.json=./xxxxxxxx.json
```
- ./xxxxxxxx.json 은 아까 생성된 cert json이다.

## ConfigMap 생성
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cloudflared-config
  namespace: cloudflare

data:
  config.yaml: |
    tunnel: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx # 터널 UUID (json 파일명)

    credentials-file: /etc/cloudflared/credentials.json # 마운트되는 시크릿, 항상 고정

    ingress:
      - hostname: "*.example.com" # 와일드카드 문법으로 URL 요청 전부 받기
        service: http://ingress-nginx-controller.ingress-nginx.svc.cluster.local:80 # ingress별로 서비스 URL

      - service: http_status:404
```
```bash
kubectl apply -f configmap.yaml
```

## Deployment 생성
```yaml
apiVersion: apps/v1   # Deployment 리소스를 사용 (앱 배포용 API 버전)
kind: Deployment      # Kubernetes에서 Pod를 관리하는 Deployment 객체
metadata:
  name: cloudflared   # Deployment 이름 (클러스터 내 식별자)
  namespace: cloudflare  # 이 리소스가 속할 네임스페이스

spec:
  replicas: 1  # Pod를 1개만 유지 (죽으면 자동 재생성)

  selector:
    matchLabels:
      app: cloudflared  # 아래 template의 label과 반드시 일치해야 함 (Pod 선택 기준)

  template:  # 실제 생성될 Pod의 템플릿
    metadata:
      labels:
        app: cloudflared  # selector와 매칭되는 Pod label

    spec:
      containers:
      - name: cloudflared  # 컨테이너 이름
        image: cloudflare/cloudflared:latest  # Cloudflare Tunnel 공식 이미지 (latest 사용)

        args:
          - tunnel
          - --config
          - /etc/cloudflared/config.yaml  # 컨테이너 내부 config 경로 지정
          - run  # tunnel 실행 명령

        volumeMounts:
        - name: config  # 아래 volumes에 정의된 config 볼륨 사용
          mountPath: /etc/cloudflared/config.yaml  # 컨테이너 내부에서 보이는 경로
          subPath: config.yaml  # ConfigMap 안에서 특정 파일만 단일 파일로 마운트

        - name: credentials  # Secret 볼륨
          mountPath: /etc/cloudflared/credentials.json  # 인증서 파일 위치
          subPath: credentials.json  # Secret 안에서 특정 파일만 사용

      volumes:
      - name: config  # ConfigMap 기반 볼륨 정의
        configMap:
          name: cloudflared-config  # 미리 만들어둔 ConfigMap 이름

      - name: credentials  # Secret 기반 볼륨 정의
        secret:
          secretName: cloudflare-tunnel  # Cloudflare Tunnel 인증 정보가 들어있는 Secret
```
```bash
kubectl apply -f cloudflared.yaml
```