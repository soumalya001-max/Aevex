class EscalationAgent:

    @staticmethod
    def escalate(task, target):

        return (
            f"I attempted '{task}' "
            f"for '{target}' several times "
            f"but could not verify success."
        )