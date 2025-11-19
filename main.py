from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.auth_route import router as auth_router
from routers.user_route import router as user_router
from routers.post_route import router as post_router
from routers.comment_route import router as comment_router

app = FastAPI(
    title="Community API",
    description="커뮤니티 백엔드 기능 테스트용 API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)