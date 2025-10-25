# create_order_test.py
import sender_stand_request
import data

class TestOrderAutomation:
    
    def test_create_order_and_get_by_track(self):
        """
        Автотест для сценария:
        1. Создать заказ
        2. Получить трек номер
        3. Получить заказ по треку
        4. Проверить статус код и данные заказа
        """
        
        # Создаем заказ
        order_response = sender_stand_request.post_order(data.order_body)
        assert order_response.status_code == 201, f"Ошибка создания заказа: {order_response.status_code}"
        
        # Получаем трек номер
        track_number = order_response.json()["track"]
        print(f"Трек номер созданного заказа: {track_number}")
        
        # Получаем заказ по треку
        track_response = sender_stand_request.get_order_by_track(track_number)
        
        # Проверяем статус код
        assert track_response.status_code == 200, f"Ошибка получения заказа: {track_response.status_code}"
        
        # Проверяем данные заказа
        order_data = track_response.json()["order"]
        assert order_data["firstName"] == data.order_body["firstName"], "Имя не совпадает"
        assert order_data["lastName"] == data.order_body["lastName"], "Фамилия не совпадает"
        
        print("✅ Все проверки пройдены успешно!")

# Для запуска через pytest нужно использовать правильный синтаксис
def test_order_creation_pytest():
    """Тест для запуска через pytest"""
    
    # Создаем заказ
    order_response = sender_stand_request.post_order(data.order_body)
    assert order_response.status_code == 201
    
    # Получаем трек номер
    track_number = order_response.json()["track"]
    
    # Получаем заказ по треку
    track_response = sender_stand_request.get_order_by_track(track_number)
    
    # Проверяем статус код
    assert track_response.status_code == 200
    
    # Проверяем данные заказа
    order_data = track_response.json()["order"]
    assert order_data["firstName"] == data.order_body["firstName"]
    assert order_data["lastName"] == data.order_body["lastName"]
    
    print(f"✅ Pytest тест пройден! Трек: {track_number}")

# Запуск автотеста (если файл запускается напрямую)
if __name__ == "__main__":
    test = TestOrderAutomation()
    test.test_create_order_and_get_by_track()