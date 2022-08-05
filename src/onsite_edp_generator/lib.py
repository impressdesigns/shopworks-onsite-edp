from typing import Final

from onsite_edp_generator.models import PaymentBlockModel

TAG_BRACKET: Final[str] = "----"
DATA_SEPERATOR: Final[str] = ": "
CARRIAGE_RETURN: Final[str] = "<cr>"

REQUIRED_BLOCKS: Final[list[str]] = [
    'Order',
    'Customer',
]
VALID_BLOCKS: Final[list[str]] = [
    'Order',
    'Customer',
    'Contact',
    'Design',
    'Products',
    'Payment',
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


if __name__ == '__main__':
    payment_data = {
        "date_Payment": "05/25/2000",
    }
    payment_model = PaymentBlockModel(**payment_data).dict()
    print(_build_block("Payment", payment_model))
