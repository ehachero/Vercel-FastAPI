from fastapi import FastAPI

app=FastAPI()

@app.get("/")

async def info ():
    return ("subimos el proyecto a vercel")

