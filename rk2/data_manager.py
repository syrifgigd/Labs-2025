from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass
class OperatingSystem:
    id: int
    name: str
    version: str

@dataclass
class Computer:
    id: int
    brand: str
    ram_gb: int
    os_id: int

@dataclass
class ComputerOS:
    computer_id: int
    os_id: int

class DataManager:
    def __init__(self,
                 operating_systems: List[OperatingSystem] = None,
                 computers: List[Computer] = None,
                 computer_os_relations: List[ComputerOS] = None):

        self.operating_systems = operating_systems or [
            OperatingSystem(1, "Windows", "11"),
            OperatingSystem(2, "Linux", "Ubuntu 22.04"),
            OperatingSystem(3, "macOS", "Ventura"),
            OperatingSystem(4, "Windows", "10"),
        ]

        self.computers = computers or [
            Computer(1, "Dell", 16, 1),
            Computer(2, "HP", 8, 1),
            Computer(3, "Lenovo", 32, 2),
            Computer(4, "Apple", 16, 3),
            Computer(5, "Asus", 8, 4),
        ]

        self.computer_os_relations = computer_os_relations or [
            ComputerOS(1, 1),
            ComputerOS(1, 2),
            ComputerOS(2, 1),
            ComputerOS(3, 2),
            ComputerOS(3, 4),
            ComputerOS(4, 3),
            ComputerOS(5, 1),
            ComputerOS(5, 4),
        ]

    def get_one_to_many_relations(self) -> List[Tuple[Computer, OperatingSystem]]:
        """Получить связи один-ко-многим (компьютер -> основная ОС)"""
        result = []
        for computer in self.computers:
            os_obj = next((os for os in self.operating_systems if os.id == computer.os_id), None)
            if os_obj:
                result.append((computer, os_obj))
        return result

    def get_os_computer_count(self) -> Dict[str, int]:
        """Получить количество компьютеров для каждой ОС"""
        os_computer_count = {}
        for os in self.operating_systems:
            count = len([comp for comp in self.computers if comp.os_id == os.id])
            os_computer_count[os.name] = count
        return os_computer_count

    def get_computers_with_ov_brand_and_os(self) -> List[Tuple[Computer, List[OperatingSystem]]]:
        """Получить компьютеры с брендом на 'ov' и их ОС"""
        result = []

        for computer in self.computers:
            if computer.brand.endswith('ov'):
                os_relations = [rel for rel in self.computer_os_relations
                               if rel.computer_id == computer.id]

                operating_systems_for_computer = []
                for rel in os_relations:
                    os_obj = next((os for os in self.operating_systems
                                 if os.id == rel.os_id), None)
                    if os_obj:
                        operating_systems_for_computer.append(os_obj)

                result.append((computer, operating_systems_for_computer))

        return result

    def display_one_to_many_relations(self, sorted_by_brand: bool = True):
        """Вывести связи один-ко-многим"""
        result = self.get_one_to_many_relations()

        if sorted_by_brand:
            result.sort(key=lambda x: x[0].brand)

        for computer, os_obj in result:
            print(f"Компьютер: {computer.brand} (ОЗУ: {computer.ram_gb}GB) -> "
                  f"ОС: {os_obj.name} {os_obj.version}")

    def display_os_computer_count(self, sorted_by_count: bool = True):
        """Вывести количество компьютеров по ОС"""
        os_computer_count = self.get_os_computer_count()

        if sorted_by_count:
            sorted_items = sorted(os_computer_count.items(), key=lambda x: x[1], reverse=True)
        else:
            sorted_items = os_computer_count.items()

        for os_name, count in sorted_items:
            print(f"ОС: {os_name} -> Количество компьютеров: {count}")

    def display_computers_with_ov_brand(self):
        """Вывести компьютеры с брендом на 'ov' и их ОС"""
        result = self.get_computers_with_ov_brand_and_os()

        for computer, os_list in result:
            os_names = ", ".join([f"{os.name} {os.version}" for os in os_list])
            print(f"Компьютер: {computer.brand} (ОЗУ: {computer.ram_gb}GB) -> "
                  f"Установленные ОС: {os_names}")

        if not result:
            print("Компьютеры с брендом, заканчивающимся на 'ov', не найдены.")
