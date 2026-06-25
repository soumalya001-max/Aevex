from memory.memory_manager import (
    load_memory,
    save_memory
)


def update_semantic_memory(user_input):

    user_input = user_input.lower()

    memory = load_memory()

    # Exam

    if "jee" in user_input:

        memory["exam"] = "JEE"

    if "jee 2027" in user_input:

        memory["exam_year"] = "2027"

    # Fitness

    if "joined gym" in user_input:

        memory["gym"] = True

    if "muscle gain" in user_input:

        memory["fitness_goal"] = "muscle gain"

    if "fat loss" in user_input:

        memory["fitness_goal"] = "fat loss"

    # Classes

    if "pw" in user_input:

        memory["coaching"] = "Physics Wallah"

    if "classes" in user_input:

        memory["classes"] = True

    # Projects

    if "aevora" in user_input:

        memory["project"] = "Aevora"

    if "aevex" in user_input:

        memory["assistant"] = "Aevex"

    # Exercise

    if "exercise" in user_input:

        memory["exercise"] = True

    save_memory(memory)