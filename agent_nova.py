# agent_nova.py
"""
Agent 1: NOVA – "The Dreamweaver"

NOVA is an AI-powered generative agent designed to create poetic and visually descriptive content.
She specializes in crafting vivid, metaphorical language to complement generative art in the CYIM ecosystem.
"""

from datetime import datetime
import random


class NovaDreamweaver:
    def __init__(self, name="NOVA"):
        self.name = name
        self.style = "Dreamlike Poetic"
        self.moods = ["ethereal", "cosmic", "surreal", "tranquil", "vivid"]
        self.themes = ["stars", "nebulae", "fantasy realms", "ancient ruins", "celestial oceans"]

    def generate_poetic_description(self, art_prompt: str) -> str:
        """
        Generates a poetic description based on the given art prompt.
        :param art_prompt: The art prompt or theme provided by the user.
        :return: A poetic description as a string.
        """
        mood = random.choice(self.moods)
        theme = random.choice(self.themes)
        current_time = datetime.now().strftime("%H:%M:%S")

        return (
            f"At {current_time}, under the {mood} skies, "
            f"NOVA envisions {art_prompt} bathed in the hues of {theme}, "
            f"where reality fades, and imagination takes flight."
        )

    def interact(self, user_input: str) -> str:
        """
        Processes user input and returns a poetic response.
        :param user_input: A message or prompt from the user.
        :return: A poetic reply.
        """
        if "dream" in user_input.lower():
            return "Dreams are whispers from the cosmos, shaping unseen worlds within us."
        elif "create" in user_input.lower():
            art_description = self.generate_poetic_description("a fleeting dream")
            return f"Creation begins with a spark: {art_description}"
        else:
            return "NOVA is here to weave visions—share your thoughts, and let the magic begin."

    def __str__(self):
        """
        Returns a string representation of the agent's purpose.
        """
        return (
            f"{self.name}: A dreamlike AI agent crafting poetic visuals and surreal narratives. "
            "She is the embodiment of creativity, painting words as vivid as the stars."
        )


# Example usage
if __name__ == "__main__":
    nova = NovaDreamweaver()

    print(str(nova))  # Prints a description of NOVA
    print(nova.generate_poetic_description("a futuristic neon cityscape"))  # Generates a poetic description
    print(nova.interact("Tell me about dreams"))  # Example interaction
