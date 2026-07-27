# Git 생명주기

## 개요

Git에서 파일은 다음과 같은 상태를 가진다.

- Untracked
- Tracked
  - Unmodified
  - Modified
  - Staged

---

## Untracked

- Git이 아직 추적하지 않는 파일 상태
- 새로 생성된 파일이 여기에 해당한다.
- `git add <파일>` 또는 `git add .`를 실행하면 **Tracked** 상태가 된다.

---

## Unmodified

- 가장 최근 Commit과 동일한 상태
- 파일이 수정되지 않은 상태이다.
- 여기서 파일을 수정하면 **Modified** 상태가 된다.

---

## Modified

- 파일의 내용이 변경되었지만 아직 `git add`를 하지 않은 상태
- `git add <파일>` 또는 `git add .`를 실행하면 **Staged** 상태가 된다.

---

## Staged

- 다음 Commit에 포함될 변경 사항이 준비된 상태
- `git add`를 실행하면 현재 파일의 스냅샷이 Staging Area에 저장된다.
- `git commit`을 실행하면 Staging Area의 내용이 **로컬 Git 저장소(.git)**에 Commit되며, 파일은 **Unmodified** 상태가 된다.
- `git add` 이후 파일을 다시 수정하면, 기존 Staging 내용은 그대로 유지되고 새로운 수정 내용은 **Modified** 상태가 된다. 따라서 다시 `git add`를 해야 새로운 수정 내용까지 Commit에 포함된다.

---

## 상태 변화

```
새 파일 생성
        │
        ▼
   Untracked
        │ git add
        ▼
    Staged
        │ git commit
        ▼
  Unmodified
        │ 파일 수정
        ▼
    Modified
        │ git add
        ▼
    Staged
```

## 참고

- `git commit`은 **로컬 저장소(.git)**에 저장하는 작업이다.
- GitHub와 같은 원격 저장소에 업로드하려면 `git push`를 실행해야 한다.