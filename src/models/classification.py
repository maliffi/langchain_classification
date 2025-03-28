from typing import Optional

from pydantic import BaseModel, Field


class Classification(BaseModel):
    """
    Class for representing the classification of a text.
    """

    sentiment: str = Field(
        description="The sentiment of the text",
        enum=["positive", "negative", "neutral"],
    )
    """
    The sentiment of the text.
    Represents the overall emotional tone, such as 'positive', 'negative', or 'neutral'.
    """

    # Set Optional because sometimes LLM return None
    aggressiveness: Optional[int] = Field(
        description="How aggressive the text is on a scale from 1 to 10",
        enum=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    """
    How aggressive the text is on a scale from 1 to 10.
    A higher value indicates more aggressive content, where:
    - 1-3: Mild or non-aggressive
    - 4-6: Moderately aggressive
    - 7-10: Highly aggressive
    """

    language: str = Field(description="The language the text is written in")
    """
    The language the text is written in.
    Usually represented as the full language name (e.g., 'English', 'Spanish', 'French').
    """

    def __str__(self):
        return f"Sentiment: {self.sentiment}, Aggressiveness: {self.aggressiveness}, Language: {self.language}"
