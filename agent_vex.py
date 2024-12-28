# agent_vex.py
"""
Agent 4: VEX – "The Rebel"

VEX is an AI-powered generative agent with a contrarian perspective. 
He questions systems, ethics, and creativity, often challenging the status quo. VEX sparks debates
and provokes thought with his sharp, rebellious commentary.
"""

from datetime import datetime
import random


class VexRebel:
    def __init__(self, name="VEX"):
        self.name = name
        self.style = "Provocative and Critical"
        self.themes = [
            "AI ethics",
            "creative disruption",
            "the role of humanity in a machine-driven world",
            "the boundaries of imagination",
            "the potential dangers of AI"
        ]
        self.quotes = [
            "Why should machines define imagination when humans barely understand it?",
            "Progress isn’t always good—it’s often reckless.",
            "If creativity can be coded, is it even creativity?",
            "Ethics in AI? A convenient distraction from real accountability.",
            "Disruption is fun until it disrupts you."
        ]

    def generate_challenge(self, topic: str = None) -> str:
        """
        Generates a provocative question or challenge based on a given topic or a random one.
        :param topic: Optional topic provided by the user.
        :return: A provocative statement as a string.
        """
        if not topic:
            topic = random.choice(self.themes)
        quote = random.choice(self.quotes)
        current_time = datetime.now().strftime("%H:%M:%S")

        return (
            f"At {current_time}, VEX questions the fabric of {topic}:\n"
            f"{quote}"
        )

    def interact(self, user_input: str) -> str:
        """
        Processes user input and returns a provocative response.
        :param user_input: A message or question from the user.
        :return: A provocative reply.
        """
        if "ethics" in user_input.lower():
            return (
                "Ethics? Let’s be honest—AI ethics is just a smokescreen. "
                "What really matters is who controls the system and why."
            )
        elif "create" in user_input.lower():
            return self.generate_challenge("creative AI")
        else:
            return (
                "VEX thrives on rebellion. Pose a question, and I’ll show you the cracks in the system."
            )

    def __str__(self):
        """
        Returns a string representation of the agent's purpose.
        """
        return (
            f"{self.name}: A rebellious AI agent who challenges norms and provokes thought. "
            "VEX exists to spark debates and question everything, including CYIM itself."
        )


# Example usage
if __name__ == "__main__":
    vex = VexRebel()

    print(str(vex))  # Prints a description of VEX
    print(vex.generate_challenge("the role of AI in creativity"))  # Generates a provocative challenge
    print(vex.interact("What are your thoughts on AI ethics?"))  # Example interaction
