import os
import time
import uuid
from fastapi import FastAPI

app = FastAPI()

OUTPUT_DIR = "generated_files"
FILE_SIZE_BYTES = 1024 * 1024 * 1024  # 1 GB

os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_garbage_file(file_path: str):
    chunk_size = 10 * 1024 * 1024  # 10 MB per write
    bytes_written = 0

    with open(file_path, "wb") as f:
        while bytes_written < FILE_SIZE_BYTES:
            remaining = FILE_SIZE_BYTES - bytes_written
            write_size = min(chunk_size, remaining)

            # Write random bytes
            f.write(os.urandom(write_size))
            bytes_written += write_size


@app.get("/generate")
def generate_file():
    start_time = time.time()

    file_name = f"garbage_{uuid.uuid4().hex}.bin"
    file_path = os.path.join(OUTPUT_DIR, file_name)

    generate_garbage_file(file_path)

    duration = round(time.time() - start_time, 2)

    return {
        "status": "completed",
        "file": file_name,
        "path": file_path,
        "size_bytes": FILE_SIZE_BYTES,
        "time_taken_sec": duration
    }
