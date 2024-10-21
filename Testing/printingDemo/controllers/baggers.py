from classes.main import Bagger, Order
from typing import List
import socket

class Baggers:

    catalog: List[Bagger] = [
        Bagger('Bagger 001', '192.168.100.200'),
        Bagger('Bagger 002', '192.168.100.204'),
        Bagger('Bagger 003', '192.168.100.199')
        ]
    selected: Bagger = None

    client = None

    def setClient(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.selected.address, 9100))
        except socket.error as e:
            print(f"Socket error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def printCatalog(self) -> None:
        for i,b in enumerate(self.catalog):
            print(f'Option: {i + 1} - Name:{b.name}')

    def setSelected(self, option:int) -> None:
        if option < 1:
            raise ValueError()
        self.selected = self.catalog[option - 1]
        self.setClient()

    def sendToPrinter(self,order:Order) -> None:
        zpl_raw = self.getFormat(order.type)
        zpl_ready = self.transformFormat(order, zpl_raw)

        try:
            self.client.sendall(zpl_ready.encode())
        except socket.error as e:
            print(f"Socket error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def getFormat(self, type: int) -> str:
        path = f'../zpl_templates/000{type}.zpl'
        result = ''

        with open(path, 'r') as file:
            result = file.read()

        return result
    
    def transformFormat(self,order:Order, zpl:str) -> str:
        result = zpl.format(
            name=order.name, 
            number=order.number,
            qr=f'Nombre:{order.name},Number:{order.number}')
        return result