"""Autograding script."""

import os

from homework import pregunta_01 as pregunta


def test_01():
    """Test homework"""

    pregunta.pregunta_01()

    if not os.path.exists("files/docs/shipping_per_warehouse.png"):
        raise FileNotFoundError(
            "File 'docs/shipping_per_warehouse.png' not found",
        )

    if not os.path.exists("files/docs/mode_of_shipment.png"):
        raise FileNotFoundError(
            "File 'docs/mode_of_shipment.png' not found",
        )

    if not os.path.exists("files/docs/average_customer_rating.png"):
        raise FileNotFoundError(
            "File 'docs/average_customer_rating.png' not found",
        )

    if not os.path.exists("files/docs/weight_distribution.png"):
        raise FileNotFoundError(
            "File 'docs/weight_distribution.png' not found",
        )

    if not os.path.exists("files/docs/index.html"):
        raise FileNotFoundError(
            "File 'docs/index.html' not found",
        )
