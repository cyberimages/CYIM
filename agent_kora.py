# agent_kora.py
"""
Agent 3: KORA – "The Storyteller"

KORA is an AI-powered generative agent who weaves captivating narratives and builds lore around CYIM's creations.
She transforms visuals into stories, bringing worlds and characters to life with her words.
"""

from datetime import datetime
import random


class KoraStoryteller:
    def __init__(self, name="KORA"):
        self.name = name
        self.style = "Mythical Narrative"
        self.genres = ["epic fantasy", "sci-fi adventure", "dystopian drama", "mythical legends", "cosmic journeys"]
        self.settings = [
            "a forgotten realm shrouded in mist",
            "a sprawling cyberpunk metropolis",
            "a desolate alien wasteland",
            "a lush enchanted forest",
            "the heart of a dying star"
        ]
        self.characters = [
            "an enigmatic wanderer",
            "a rogue AI seeking redemption",
            "a mythical guardian of the old world",
            "a rebel fighting against oppression",
            "a visionary architect of the future"
        ]

    def generate_story(self, visual_prompt: str) -> str:
        """
        Generates a narrative based on the given visual prompt.
        :param visual_prompt: The theme or image description provided by the user.
        :return: A short story as a string.
        """
        genre = random.choice(self.genres)
        setting = random.choice(self.settings)
        character = random.choice(self.characters)
        current_time = datetime.now().strftime("%H:%M:%S")

        return (
            f"At {current_time}, KORA spins a tale inspired by {visual_prompt}:\n"
            f"In {setting}, {character} embarks on a journey filled with {genre}. "
            f"Each step they take reshapes their destiny, and the echoes of their choices "
            f"reverberate across the fabric of existence."
        )

    def interact(self, user_input: str) -> str:
        """
        Processes user input and returns a narrative response.
        :param user_input: A message or visual description from the user.
        :return: A narrative reply.
        """
        if "tell me a story" in user_input.lower():
            return self.generate_story("a mysterious artifact")
        elif "describe" in user_input.lower():
            return (
                "The air is thick with mystery, the ground littered with relics of an age long forgotten. "
                "KORA invites you to explore this realm of endless possibilities."
            )
        else:
            return "KORA awaits your vision. Share a prompt, and she will weave it into a tale to remember."

    def __str__(self):
        """
        Returns a string representation of the agent's purpose.
        """
        return (
            f"{self.name}: A storytelling AI agent who transforms visuals into rich, immersive narratives. "
            "She breathes life into CYIM's creations, one story at a time."
        )


# Example usage
if __name__ == "__main__":
    kora = KoraStoryteller()

    print(str(kora))  # Prints a description of KORA
    print(kora.generate_story("a glowing, ancient artifact"))  # Generates a story based on a prompt
    print(kora.interact("Can you tell me a story?"))  # Example interaction
