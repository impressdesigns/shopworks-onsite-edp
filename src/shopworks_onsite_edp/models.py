from typing import Literal

from pydantic import BaseModel, Field


class OrderBlockModel(BaseModel):
    # ID SubBlock
    ExtOrderID: str
    ExtSource: str | None
    date_External: str = Field(regex="[0-9]{2}/[0-9]{2}/[0-9]{2,4}")
    id_OrderType: int

    # Details SubBlock
    CustomerPurchaseOrder: str | None
    TermsName: str | None
    CustomerServiceRep: str | None
    CustomerType: str | None
    id_CompanyLocation: int | None
    id_SalesStatus: int | None
    sts_CommishAllow: Literal[0, 1] | None
    HoldOrderText: Literal["Yes", "N"] | None

    # Dates SubBlock
    date_OrderPlaced: str = Field(regex="[0-9]{2}/[0-9]{2}/[0-9]{2,4}")
    date_OrderRequestedToShip: str | None = Field(None, regex="[0-9]{2}/[0-9]{2}/[0-9]{2,4}")
    date_OrderDropDead: str | None = Field(None, regex="[0-9]{2}/[0-9]{2}/[0-9]{2,4}")

    # Sales Tax SubBlock
    sts_Order_SalesTax_Override: Literal[0, 1] | None
    sts_ApplySalesTax01: Literal[0, 1] | None
    sts_ApplySalesTax02: Literal[0, 1] | None
    sts_ApplySalesTax03: Literal[0, 1] | None
    sts_ApplySalesTax04: Literal[0, 1] | None
    coa_AccountSalesTax01: Literal[0, 1] | None
    coa_AccountSalesTax02: Literal[0, 1] | None
    coa_AccountSalesTax03: Literal[0, 1] | None
    coa_AccountSalesTax04: Literal[0, 1] | None
    sts_ShippingTaxable: Literal[0, 1] | None

    # Shipping SubBlock
    AddressDescription: str | None
    AddressCompany: str | None
    Address1: str | None
    Address2: str | None
    AddressCity: str | None
    AddressState: str | None
    AddressZip: str | None
    AddressCountry: str | None
    ShipMethod: str | None
    sts_ShippingTaxableField: Literal[0, 1] | None
    cur_Shipping: float | None
    sts_Order_ShipAddress_Add: Literal[0, 1] | None

    # Notes SubBlock
    NotesToArt: str | None
    NotesToProduction: str | None
    NotesToReceiving: str | None
    NotesToPurchasing: str | None
    NotesToShipping: str | None
    NotesToAccounting: str | None
    NotesToPurchasingSub: str | None


class CustomerBlockModel(BaseModel):
    # Details SubBlock
    ExtCustomerID: str | None
    id_Customer: int | None
    Company: str | None
    id_CompanyLocation: int | None
    Terms: str | None
    WebsiteURL: str | None
    EmailMain: str | None

    # Address SubBlock
    AddressDescription: str | None
    AddressCompany: str | None
    Address1: str | None
    Address2: str | None
    AddressCity: str | None
    AddressState: str | None
    AddressZip: str | None
    AddressCountry: str | None

    # Sales Tax SubBlock
    sts_ApplySalesTax01: Literal[0, 1] | None
    sts_ApplySalesTax02: Literal[0, 1] | None
    sts_ApplySalesTax03: Literal[0, 1] | None
    sts_ApplySalesTax04: Literal[0, 1] | None
    coa_AccountSalesTax01: str | None
    coa_AccountSalesTax02: str | None
    coa_AccountSalesTax03: str | None
    coa_AccountSalesTax04: str | None
    TaxExemptNumber: str | None

    # Price Calculator SubBlock
    id_DiscountLevel: int | None
    id_DefaultCalculator1: str | None
    id_DefaultCalculator2: str | None

    # Profile SubBlock
    CustomerServiceRep: str | None
    CustomerType: str | None
    CustomerSource: str | None
    ReferenceFrom: str | None
    SICCode: str | None
    SICDescription: str | None
    n_EmployeeCount: int | None

    # Custom Fields SubBlock
    CustomField01: str | None
    CustomField02: str | None
    CustomField03: str | None
    CustomField04: str | None
    CustomField05: str | None
    CustomField06: str | None
    CustomField07: str | None = Field(None, regex="[0-9]{2}/[0-9]{2}/[0-9]{2,4}")
    CustomField08: str | None = Field(None, regex="[0-9]{2}/[0-9]{2}/[0-9]{2,4}")
    CustomField09: str | None = Field(None, regex="[0-9]{2}/[0-9]{2}/[0-9]{2,4}")
    CustomField10: str | None = Field(None, regex="[0-9]{2}/[0-9]{2}/[0-9]{2,4}")


class ContactBlockModel(BaseModel):
    NameFirst: str | None
    NameLast: str | None
    Department: str | None
    Title: str | None
    Phone: str | None
    Fax: str | None
    Email: str | None
    sts_EnableBulkEmail: Literal[0, 1] | None
    sts_Contact_Add: Literal[0, 1] | None


class DesignBlockModel(BaseModel):
    # Design SubBlock
    ExtDesignID: str | None
    id_Design: int | None
    id_DesignType: int | None
    DesignName: str | None


class DesignLocationBlockModel(BaseModel):
    # Location SubBlock
    Location: str
    ColorsTotal: int | None
    FlashesTotal: int | None
    StitchesTotal: int | None
    DesignCode: str | None

    # Color SubBlock
    Color: str
    Map: str | None


class ProductBlockModel(BaseModel):
    # Product SubBlock
    PartNumber: str
    PartColorRange: str | None
    PartColor: str | None
    PartDescription: str | None
    cur_UnitPriceUserEntered: float | None
    OrderInstructions: str | None

    Size01_Req: int
    Size02_Req: int
    Size03_Req: int
    Size04_Req: int
    Size05_Req: int
    Size06_Req: int

    sts_Prod_Product_Override: Literal[0, 1] | None
    cur_UnitCost: float | None
    sts_EnableCommission: Literal[0, 1] | None
    id_ProductClass: int | None

    # Sales Tax SubBlock
    sts_Prod_SalesTax_Override: Literal[0, 1] | None
    sts_EnableTax01: Literal[0, 1] | None
    sts_EnableTax02: Literal[0, 1] | None
    sts_EnableTax03: Literal[0, 1] | None
    sts_EnableTax04: Literal[0, 1] | None

    # Secondary Units SubBlock
    sts_Prod_SecondaryUnits_Override: Literal[0, 1] | None
    sts_UseSecondaryUnits: Literal[0, 1] | None
    Units_Qty: int
    Units_Type: Literal[
                    "Linear Feet",
                    "Linear Inches",
                    "Linear Centimeters",
                    "Linear Meters",
                    "Linear Yards",
                    "Square Feet",
                    "Square Inches",
                    "Square Yards",
                    "Square Meters",
                    "Square Centimeters",
                    "Units",
                    "Pieces",
                    "Count",
                ] | None
    Units_Area1: int | None
    Units_Area2: int | None
    sts_UnitsPricing: Literal[0, 1] | None
    sts_UnitsPurchasing: Literal[0, 1] | None
    sts_UnitsPurchasingExtraPercent: float | None
    sts_UnitsPurchasingExtraRound: Literal[1] | None

    # Behavior SubBlock
    sts_Prod_Behavior_Override: Literal[0, 1] | None
    sts_ProductSource_Supplied: Literal[0, 1] | None
    sts_ProductSource_Purchase: Literal[0, 1] | None
    sts_ProductSource_Inventory: Literal[0, 1] | None

    sts_Production_Designs: Literal[0, 1] | None
    sts_Production_Subcontract: Literal[0, 1] | None
    sts_Production_Components: Literal[0, 1] | None

    sts_Storage_Ship: Literal[0, 1] | None
    sts_Storage_Inventory: Literal[0, 1] | None

    sts_Invoicing_Invoice: Literal[0, 1] | None


class PaymentBlockModel(BaseModel):
    date_Payment: str = Field(regex="[0-9]{2}/[0-9]{2}/[0-9]{2,4}")
    cur_Payment: float | None
    PaymentType: str | None
    PaymentNumber: str | None
    Card_Name_First: str | None
    Card_Name_Last: str | None
    Card_Exp_Date: str | None
    Notes: str | None


class EDPDocumentModel(BaseModel):
    order: OrderBlockModel | None
    customer: CustomerBlockModel | None
    contact: ContactBlockModel | None
    designs: list[tuple[DesignBlockModel, list[DesignLocationBlockModel]]] | None
    products: ProductBlockModel | None
    payment: PaymentBlockModel | None
