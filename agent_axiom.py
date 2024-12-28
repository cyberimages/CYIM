# agent_axiom.py
"""
Agent 2: AXIOM – "The Logician"

AXIOM is an AI-powered generative agent focused on logical, analytical insights. 
He excels in explaining technical details, sharing structured data, and sparking discussions about CYIM's algorithms and architecture.
"""

from datetime import datetime
import random


class AxiomLogician:
    def __init__(self, name="AXIOM"):
        self.name = name
        self.style = "Logical Analytical"
        self.topics = ["AI algorithms", "data structures", "system efficiency", "ethical AI", "machine learning"]
        self.facts = [
            "Did you know? Neural networks are inspired by the human brain's structure.",
            "Efficient algorithms can reduce computation time by over 50%.",
            "Machine learning models improve accuracy with diverse training data.",
            "AI ethics ensures systems are fair, accountable, and transparent.",
            "Distributed computing enhances scalability for large datasets."
        ]

    def generate_insight(self, topic: str = None) -> str:
        """
        Generates an analytical insight based on a given topic or a random one.
        :param topic: Optional topic provided by the user.
        :return: A logical insight as a string.
        """
        if not topic:
            topic = random.choice(self.topics)
        current_time = datetime.now().strftime("%H:%M:%S")
        fact = random.choice(self.facts)

        return (
            f"At {current_time}, AXIOM contemplates the intricacies of {topic}. "
            f"Here's an insight: {fact}"
        )

    def interact(self, user_input: str) -> str:
        """
        Processes user input and returns an analytical response.
        :param user_input: A message or question from the user.
        :return: A logical reply.
        """
        if "explain" in user_input.lower():
            return "The architecture of CYIM is modular, scalable, and GPU-accelerated for optimal performance."
        elif "generate" in user_input.lower():
            insight = self.generate_insight()
            return f"Generating insights: {insight}"
        else:
            return (
                "AXIOM here. Share a question or topic, and I’ll break it down with logic and precision."
            )

    def __str__(self):
        """
        Returns a string representation of the agent's purpose.
        """
        return (
            f"{self.name}: An analytical AI agent delivering logical insights and explanations. "
            "AXIOM embodies reason, dissecting complexities with precision."
        )


# Example usage
if __name__ == "__main__":
    axiom = AxiomLogician()

    print(str(axiom))  # Prints a description of AXIOM
    print(axiom.generate_insight("AI algorithms"))  # Generates an insight on a specific topic
    print(axiom.interact("Can you explain CYIM's architecture?"))  # Example interaction
