def classify_task(prompt):

    prompt = prompt.lower()

    command_keywords = [

        "open",
        "shutdown",
        "restart",
        "create folder",
        "delete file",
        "rename file"

    ]

    coding_keywords = [

        "code",
        "website",
        "python",
        "html",
        "css",
        "javascript"

    ]

    reasoning_keywords = [

        "why",
        "how",
        "explain",
        "solve",
        "physics",
        "math"

    ]

    for word in command_keywords:

        if word in prompt:

            return "command"

    for word in coding_keywords:

        if word in prompt:

            return "coding"

    for word in reasoning_keywords:

        if word in prompt:

            return "reasoning"

    return "general"