import os
import uvicorn

from business.core import Core

if __name__ == '__main__':
    # workdir = os.getcwd()
    # uvicorn.run("input.input_api:app", port=50081, reload=True)
    core = Core()
    core.execute()
