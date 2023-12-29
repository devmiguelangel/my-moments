from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    """Root path."""

    return {
        'message': 'Hello World1',
        'message1': 'Hello World2',
        'message2': 'Hello World3',
        'message3': 'Hello World4',
        'message4': 'Hello World5',
    }
