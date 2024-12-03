"""Serializer module."""

from .models import EDPDocument


class Serializer:
    """Serialize the data."""

    def __init__(self, tag_bracket: str = "----", data_seperator: str = ": ", carriage_return: str = "<cr>") -> None:
        self.tag_bracket = tag_bracket
        self.data_seperator = data_seperator
        self.carriage_return = carriage_return

    def build_document(self, document: EDPDocument) -> str:
        """Serialize to text."""
        data = document.model_dump(by_alias=True, exclude_unset=True)
        text = ""

        for block_name in data:
            block_text = ""
            block_text += f"{self.tag_bracket} Start {block_name.title()} {self.tag_bracket}\n"

            for key, value in data[block_name].items():
                block_text += f"{key}{self.data_seperator}{value}\n"

            block_text += f"{self.tag_bracket} End {block_name.title()} {self.tag_bracket}\n"

            text += block_text

        return text
