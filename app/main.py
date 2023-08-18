from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import aluno_routers_v1
from routers import aluno_routers_v2

def create_app():
    app = FastAPI()

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(aluno_routers_v1.router, prefix="/v1")
    
    app.include_router(aluno_routers_v2.router)
    app.include_router(aluno_routers_v2.router, prefix="/v2")
    app.include_router(aluno_routers_v2.router, prefix="/latest")

    return app

app = create_app()