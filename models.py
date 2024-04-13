from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel


class postbackModel(BaseModel):
    dhanClientId: Any | None
    orderId: Any | None
    correlationId: Any | None
    orderStatus: Any | None
    transactionType: Any | None
    exchangeSegment: Any | None
    productType: Any | None
    orderType: Any | None
    validity: Any | None
    tradingSymbol: Any | None
    securityId: Any | None
    quantity: Any | None
    disclosedQuantity: Any | None
    price: Any | None
    triggerPrice: Any | None
    afterMarketOrder: Any | None
    boProfitValue: Any | None
    boStopLossValue: Any | None
    legName: Any | None = None
    createTime: Any | None
    updateTime: Any | None
    exchangeTime: Any | None
    drvExpiryDate: Any | None
    drvOptionType: Any | None
    drvStrikePrice: Any | None
    omsErrorCode: Any | None
    omsErrorDescription: Any | None

