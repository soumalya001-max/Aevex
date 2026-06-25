from memory.context_builder import build_context
from core.personality_manager import get_personality

from vector_memory.retriever import (
    retrieve_context
)


def build_prompt(
    user_prompt,
    task_type
):

    personality = get_personality(
        task_type
    )

    memory_context = build_context()

    rag_context = retrieve_context(
        user_prompt
    )

    prompt = f"""
{personality}

------------------------
IDENTITY + MEMORY
------------------------

{memory_context}

------------------------
RELEVANT KNOWLEDGE
------------------------

{rag_context}

------------------------
USER REQUEST
------------------------

{user_prompt}
"""

    return prompt