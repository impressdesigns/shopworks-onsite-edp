"""Test models."""

from shopworks_onsite_edp.lib import build_document
from shopworks_onsite_edp.models import CustomerBlockModel, EDPDocumentModel, OrderBlockModel


def test_can_create_order() -> None:
    """Can't access protected endpoints without all required scopes."""
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
    build_document(edp_document.model_dump(by_alias=True))
