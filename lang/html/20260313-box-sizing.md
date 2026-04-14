# box-sizing

박스 사이징을 지정하지 않을 경우
- 콘텐츠 영역의 크기만 지정

`box-sizing: border-box` 일 경우
- 박스 영역 크기가 지정됨
- 콘텐츠 영역의 크기를 빼서 계산
```
.box2 {
    box-sizing: border-box;
    width:200px;
    height:100px;
    padding:20px;
    border:10px solid #00f;
}
```
콘텐츠 영역의 가로
- 200 - 20*2 - 10*2 = 140(px)
콘텐츠 영역의 세로
- 100 - 20*2 - 10*2 = 40(px)


