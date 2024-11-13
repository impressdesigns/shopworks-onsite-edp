from typing import Final

from shopworks_onsite_edp.models import EDPDocumentModel

TAG_BRACKET: Final[str] = "----"
DATA_SEPERATOR: Final[str] = ": "
CARRIAGE_RETURN: Final[str] = "<cr>"

REQUIRED_BLOCKS: Final[list[str]] = [
    "Order",
    "Customer",
]
VALID_BLOCKS: Final[list[str]] = [
    "Order",
    "Customer",
    "Contact",
    "Design",
    "Products",
    "Payment",
]


def _build_block(block_name: str, data: dict[str, str | int | float | None]) -> str:
    if block_name not in VALID_BLOCKS:
        raise ValueError("invalid block")

    block_text = ""
    block_text += f"{TAG_BRACKET} Start {block_name} {TAG_BRACKET}\n"

    for key, value in data.items():
        if value is not None:
            block_text += f"{key}{DATA_SEPERATOR}{value}\n"

    block_text += f"{TAG_BRACKET} End {block_name} {TAG_BRACKET}\n"

    return block_text


def build_document(data: dict[str, dict[str, str | int | float | None]]) -> str:
    if not all(block.lower() in data for block in REQUIRED_BLOCKS):
        raise ValueError("not all required blocks present")
    document = ""
    for block in VALID_BLOCKS:
        if block.lower() in data and data[block.lower()] is not None:
            document += _build_block(block, data[block.lower()])
    return document


if __name__ == "__main__":
    document_data = {
        "order": {
            "ExtOrderID": "TEST",
            "date_External": "08/05/2022",
            "id_OrderType": 1,
            "date_OrderPlaced": "08/05/2022",
        },
        "customer": {
            "id_Customer": 5547,
        },
    }
    document_model = EDPDocumentModel(**document_data).dict()
    print(document_model)
    print(build_document(document_model))
