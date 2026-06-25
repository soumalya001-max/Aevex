from providers.gemini_provider import ask_gemini
from providers.groq_provider import ask_groq
from providers.openrouter_provider import ask_openrouter

question = "Say hello."

print("\n===== GEMINI =====")
print(ask_gemini(question))

print("\n===== GROQ =====")
print(ask_groq(question))

print("\n===== OPENROUTER =====")
print(ask_openrouter(question))
