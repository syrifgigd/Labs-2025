import unittest
from data_manager import DataManager, OperatingSystem, Computer, ComputerOS

class TestDataManager(unittest.TestCase):

    def setUp(self):
        """Настройка тестовых данных"""
        self.test_os = [
            OperatingSystem(1, "Windows", "11"),
            OperatingSystem(2, "Linux", "Ubuntu 22.04"),
            OperatingSystem(3, "macOS", "Ventura"),
        ]

        self.test_computers = [
            Computer(1, "Dell", 16, 1),
            Computer(2, "HP", 8, 1),
            Computer(3, "Lenovo", 32, 2),
        ]

        self.test_relations = [
            ComputerOS(1, 1),
            ComputerOS(1, 2),
            ComputerOS(2, 1),
            ComputerOS(3, 2),
        ]

        self.manager = DataManager(
            operating_systems=self.test_os,
            computers=self.test_computers,
            computer_os_relations=self.test_relations
        )

    def test_get_one_to_many_relations(self):
        """Тест 1: Проверка получения связей один-ко-многим"""
        result = self.manager.get_one_to_many_relations()

        self.assertEqual(len(result), 3)
        computer, os_obj = result[0]
        self.assertEqual(computer.id, 1)
        self.assertEqual(computer.brand, "Dell")
        self.assertEqual(os_obj.id, 1)
        self.assertEqual(os_obj.name, "Windows")

        for computer, os_obj in result:
            self.assertEqual(computer.os_id, os_obj.id)

    def test_get_os_computer_count(self):
        """Тест 2: Проверка подсчета компьютеров по ОС"""
        result = self.manager.get_os_computer_count()

        self.assertEqual(len(result), 3)
        self.assertEqual(result["Windows"], 2)
        self.assertEqual(result["Linux"], 1)
        self.assertEqual(result["macOS"], 0)
        self.assertIn("Windows", result)
        self.assertIn("Linux", result)
        self.assertIn("macOS", result)

    def test_get_computers_with_ov_brand_and_os(self):
        """Тест 3: Проверка поиска компьютеров с брендом на 'ov'"""
        result = self.manager.get_computers_with_ov_brand_and_os()

        self.assertEqual(len(result), 1)

        computer, os_list = result[0]

        self.assertEqual(computer.id, 3)
        self.assertEqual(computer.brand, "Lenovo")
        self.assertEqual(computer.ram_gb, 32)

        self.assertEqual(len(os_list), 1)
        self.assertEqual(os_list[0].id, 2)
        self.assertEqual(os_list[0].name, "Linux")

    def test_get_computers_with_ov_brand_no_results(self):
        """Тест 4: Проверка случая, когда нет компьютеров с брендом на 'ov'"""
        computers_without_ov = [
            Computer(1, "Dell", 16, 1),
            Computer(2, "HP", 8, 1),
            Computer(3, "Apple", 32, 3),
        ]

        manager = DataManager(
            operating_systems=self.test_os,
            computers=computers_without_ov,
            computer_os_relations=self.test_relations
        )

        result = manager.get_computers_with_ov_brand_and_os()

        self.assertEqual(len(result), 0)

    def test_sorting_one_to_many(self):
        """Тест 5: Проверка сортировки связей один-ко-многим"""
        result = self.manager.get_one_to_many_relations()

        sorted_result = sorted(result, key=lambda x: x[0].brand)

        brands = [computer.brand for computer, _ in sorted_result]
        self.assertEqual(brands, ["Dell", "HP", "Lenovo"])

if __name__ == '__main__':
    unittest.main()
