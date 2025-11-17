from fastapi import FastAPI
from routers.auth_route import router as auth_router
from routers.user_route import router as user_router
from routers.post_route import router as post_router
from routers.comment_route import router as comment_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)