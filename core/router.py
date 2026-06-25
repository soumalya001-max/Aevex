from core.task_classifier import classify_task
from core.prompt_builder import build_prompt

from providers.gemini_provider import ask_gemini
from providers.groq_provider import ask_groq
from providers.openrouter_provider import ask_openrouter

from commands.command_executor import execute_command

from agents.planner_agent import create_plan
from agents.executor_agent import execute_plan


def ask_ai(prompt):

    task_type = classify_task(prompt)

    print()

    print(
        f"[Task Type: {task_type}]"
    )

    # ------------------------------
    # AGENT PLANNING
    # ------------------------------

    plan = create_plan(prompt)

    tool_results = execute_plan(
        plan
    )

    tool_context = ""

    if tool_results:

        tool_context = (
            "\n".join(tool_results)
        )

    # ------------------------------
    # COMMAND ONLY
    # ------------------------------

    if task_type == "command":

        return tool_context

    # ------------------------------
    # CONTEXT BUILDING
    # ------------------------------

    enhanced_prompt = build_prompt(
         prompt,
         task_type
    )

    final_prompt = f"""

Tool Results:

{tool_context}

User Request:

{enhanced_prompt}

"""

    providers = [

        (
            "OpenRouter",
            ask_openrouter
        ),

        (
            "Groq",
            ask_groq
        ),

        (
            "Gemini",
            ask_gemini
        )

    ]

    for name, provider in providers:

        try:

            print()

            print(
                f"[Using {name}]"
            )

            return provider(
                final_prompt
            )

        except Exception as e:

            print()

            print(
                f"{name} failed"
            )

            print(e)

    return (
        "Sorry, all AI providers "
        "are unavailable."
    )