import os
import openai
from pydantic import BaseModel

openai.organization = "org-F7xuajFc7l00rI8djb2p72b9"
openai.api_key = "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"
print("[PROCESANDO INFO...]".center(40, "-"))


class Document(BaseModel):
    prompt: str = ""


def conBi(prompt: str) -> list:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """Eres un convertidor de numeros reales a binarios E.G: Matematicas
             -Es como un sistema de numeros facil de aprender""",
            },
            {"role": "user", "content": prompt},
        ],
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print("[TERMINO EL PROCESO]".center(40, "-"))
    return [content, total_tokens]
