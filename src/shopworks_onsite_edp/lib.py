"""Library for the EDP document."""

from typing import Final

from shopworks_onsite_edp.models import CustomerBlockModel, EDPDocumentModel, OrderBlockModel

TAG_BRACKET: Final[str] = "----"
DATA_SEPERATOR: Final[str] = ": "
CARRIAGE_RETURN: Final[str] = "<cr>"

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
        msg = "invalid block"
        raise ValueError(msg)

    block_text = ""
    block_text += f"{TAG_BRACKET} Start {block_name} {TAG_BRACKET}\n"

    for key, value in data.items():
        if value is not None:
            block_text += f"{key}{DATA_SEPERATOR}{value}\n"

    block_text += f"{TAG_BRACKET} End {block_name} {TAG_BRACKET}\n"

    return block_text


def build_document(data: dict[str, dict[str, str | int | float | None]]) -> str:
    """Build the document from the data."""
    document = ""
    for block in VALID_BLOCKS:
        if block.lower() in data and data[block.lower()] is not None:
            document += _build_block(block, data[block.lower()])
    return document


if __name__ == "__main__":
    edp_document = EDPDocumentModel(
        order=OrderBlockModel(
            external_order_id="TEST",
            date_external="08/05/2022",
            order_type_id=1,
            date_order_placed="08/05/2022",
        ),
        customer=CustomerBlockModel(
            customer_id=1,
        ),
    )
    print(edp_document.model_dump(by_alias=True))  # noqa: T201
    print(build_document(edp_document.model_dump(by_alias=True)))  # noqa: T201
