import os
import openai
from pydantic import BaseModel

openai.organization = "org-F7xuajFc7l00rI8djb2p72b9"
openai.api_key = "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"
print("[PROCESANDO INFO...]".center(40, "-"))


class Document(BaseModel):
    prompt: str = ""


def inference(prompt: str) -> list:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """Eres un profesor de programacion para ninios, genera
             una explicacion para el tema que se te proporciona E.G: Programacion
             -Es como armar un rompecabezas donde cada pieza forma el sistema completo""",
            },
            {"role": "user", "content": prompt},
        ],
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print("[TERMINO EL PROCESO]".center(40, "-"))
    return [content, total_tokens]
