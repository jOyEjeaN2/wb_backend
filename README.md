## [커뮤니티 백엔드]
간단한 커뮤니티 백엔드  
Route-Controller-Model 패턴 기반이며 DB 없이 임시 메모리(JSON 구조)로 동작

### 구조 

<img width="342" height="497" alt="Screenshot 2025-11-19 at 7 26 58 PM" src="https://github.com/user-attachments/assets/d241bc73-77de-44e6-9a50-f06a21f0f3e4" />


### 실행 
uvicorn main:app --reload  
http://localhost:8000/docs  


  
## [API Routes 요약]
### 1. Auth (회원가입 / 로그인)
| Method | Endpoint       | Description |
| ------ | -------------- | ----------- |
| POST   | `/auth/signup` | 회원가입        |
| POST   | `/auth/login`  | 로그인         |


### 2. Users (프로필 / 비번 / 탈퇴)
| Method | Endpoint                    | Description |
| ------ | --------------------------- | ----------- |
| PUT    | `/users/{user_id}/profile`  | 닉네임 수정      |
| PUT    | `/users/{user_id}/password` | 비밀번호 수정     |
| POST   | `/users/logout`             | 로그아웃        |
| DELETE | `/users/{user_id}`          | 회원탈퇴        |

### 3. Posts (게시글)
| Method | Endpoint                | Description        |
| ------ | ----------------------- | ------------------ |
| GET    | `/posts`                | 게시글 목록 조회 (페이징 가능) |
| POST   | `/posts`                | 게시글 생성             |
| GET    | `/posts/{post_id}`      | 게시글 상세 조회          |
| PUT    | `/posts/{post_id}`      | 게시글 수정             |
| DELETE | `/posts/{post_id}`      | 게시글 삭제             |
| POST   | `/posts/{post_id}/like` | 좋아요 토글             |

### 4. Comments (댓글)
| Method | Endpoint                 | Description  |
| ------ | ------------------------ | ------------ |
| POST   | `/comments/{post_id}`    | 댓글 작성        |
| GET    | `/comments/{post_id}`    | 특정 게시글 댓글 조회 |
| PUT    | `/comments/{comment_id}` | 댓글 수정        |
| DELETE | `/comments/{comment_id}` | 댓글 삭제        |

