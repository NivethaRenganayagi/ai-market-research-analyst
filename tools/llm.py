from groq import Groq
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_response(prompt):

    for attempt in range(3):

        try:

            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=850
            )

            return completion.choices[0].message.content

        except Exception as e:

            print(f"Retrying due to error: {e}")

            time.sleep(8)

    return "LLM generation failed."