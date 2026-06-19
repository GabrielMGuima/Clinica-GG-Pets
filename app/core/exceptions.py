from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def handler_erro_global(request: Request, exc: HTTPException):
    # Transforma o erro no formato exato que o professor exigiu no item 5.3
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "ERRO_DE_NEGOCIO" if exc.status_code == 400 else "RECURSO_NAO_ENCONTRADO",
            "message": exc.detail,
            "details": {
                "path": request.url.path,
                "status_code": exc.status_code
            }
        }
    )