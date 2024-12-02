"""Test models."""

from onsite_edp_sdk import Customer, EDPDocument, Order, Serializer


def test_can_create_order() -> None:
    """Can't access protected endpoints without all required scopes."""
    edp_document = EDPDocument(
        order=Order(
            external_order_id="TEST",
            date_external="08/05/2022",
            order_type_id=1,
            date_order_placed="08/05/2022",
        ),
        customer=Customer(
            customer_id=1,
        ),
    )
    Serializer().build_document(edp_document)
