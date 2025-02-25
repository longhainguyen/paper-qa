from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Union, Optional

StrPath = Union[str, Path]


@dataclass
class Context:
    """A class to hold the context of a question."""

    key: str
    citation: str
    context: str
    text: str
    dockey: str
    score: int = 5

    def __str__(self) -> str:
        """Return the context as a string."""
        return self.context


@dataclass
class Answer:
    """A class to hold the answer to a question."""

    question: str
    answer: str = ""
    context: str = ""
    contexts: Optional[List[Context]] = None
    references: str = ""
    formatted_answer: str = ""
    passages: Optional[Dict[str, str]] = None
    tokens: int = 0
    cost: float = 0
    key_filter: Optional[str] = None

    def __post_init__(self):
        """Initialize the answer."""
        if self.contexts is None:
            self.contexts = []
        if self.passages is None:
            self.passages = {}

    def __str__(self) -> str:
        """Return the answer as a string."""
        return self.formatted_answer
