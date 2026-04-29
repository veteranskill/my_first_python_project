def calculate_net_salary(gross_salary, tax_rate):
    """Считает чистую зарплату после налогов"""
    return gross_salary * (1 - tax_rate / 100)

def test_salary():
    # Проверяем: при зарплате 300 000 и налоге 13% должно быть 261 000
    assert calculate_net_salary(300000, 13) == 261000
    print("Тест пройден: Зарплата рассчитана верно!")

if __name__ == "__main__":
    test_salary()
