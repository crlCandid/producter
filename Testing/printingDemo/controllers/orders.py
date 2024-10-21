from classes.main import Order
from typing import List

class Orders:

    catalog: List[Order] = [
        Order(1, 'Nombre 001', 'E2EPML02'),
        Order(2, 'Nombre 002', 'E2EPML01'),
        Order(1, 'Nombre 003', 'E2EPML05'),
        Order(2, 'Nombre 004', 'E2EPML04')
    ]

    def getOrder(self, request:str) -> Order:
        result = None

        for c in self.catalog:
            if c.number == request:
                result = c
                break

        return result