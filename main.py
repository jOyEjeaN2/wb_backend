from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth_route, user_route, post_route, comment_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_route.router)
app.include_router(user_route.router)
app.include_router(post_route.router)
app.include_router(comment_route.router)
