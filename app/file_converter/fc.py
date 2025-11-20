import subprocess
import uuid
import os

from fastapi import File, UploadFile


async def file_converter(office_files: list[UploadFile] = File(...)):
    pdf_urls = []
    output_dir = "converted"
    for file in office_files:
        try:
            file_name = file.filename
            pdf_name = os.path.splitext(file_name)[0] + ".pdf"
            pdf_path = os.path.join(output_dir, pdf_name)
            temp_path = f"temp_{uuid.uuid4()}_{file_name}"
            content = await file.read()

            with open(temp_path, "wb") as buffer:
                buffer.write(content)

            subprocess.run(
                ["soffice",
                 "--headless",
                 "--convert-to", "pdf",
                 "--outdir", output_dir,
                 temp_path
                 ], check=True)

            pdf_urls.append(pdf_path)

        except Exception as e:
            raise Exception(e)

        if os.path.exists(temp_path):
            os.remove(temp_path)

    return pdf_urls
