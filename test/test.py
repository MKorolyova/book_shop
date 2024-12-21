import requests
import unittest

BASE_URL = "http://localhost:8000/data"

class TestAPIEndpoints(unittest.TestCase):

    def setUp(self):
        self.customer = {
            "email": "m@gmail.com",
            "password": "123456",
            "customer_id": 1564883732
        }

    def test_fetch_data_log_in(self):
  
        url = f"{BASE_URL}/customer/log-in/email/{self.customer['email']}/password/{self.customer['password']}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
        response_data = response.json()
        self.assertIn("customer", response_data, "Response missing 'customer' key")
        self.assertIn("customer_id", response_data["customer"], "Response missing 'customer_id' key in 'customer'")

    def test_fetch_data_rand_books(self):
        limit = 5
        url = f"{BASE_URL}/book/get-book-by-random-page/customer_id/{self.customer['customer_id']}/limit/{limit}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
        response_data = response.json()
        self.assertIn("book", response_data, "Response missing 'book' key")
        self.assertIsInstance(response_data["book"], list, "Response is not a list")

    def test_fetch_data_book_page(self):
        book_id = 62328251
        url = f"{BASE_URL}/book/get-book-page/customer_id/{self.customer['customer_id']}/book_id/{book_id}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
        response_data = response.json()
        self.assertIn("book", response_data, "Response missing 'book' key")
        self.assertIn("book_name", response_data["book"], "Response missing 'book_name' key in 'customer'")

    def test_fetch_data_genre_books_page(self):
        genre_id = 1
        url = f"{BASE_URL}/book/get-book-by-genre-page/customer_id/{self.customer['customer_id']}/genre_id/{genre_id}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
        response_data = response.json()
        self.assertIn("book", response_data, "Response missing 'book' key")
        self.assertIsInstance(response_data["book"], list, "Response is not a list")

    def test_fetch_data_add_book(self):
        book_id = 62328251
        url = f"{BASE_URL}/order-item/add-item-to-order/customer_id/{self.customer['customer_id']}/book_id/{book_id}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    def test_fetch_data_delete_book(self):
        """Проверка удаления книги из корзины."""
        order_item_id = 1807625036   # choose corect oe befor test
        url = f"{BASE_URL}/order-item/del-item-from-order/customer_id/{self.customer['customer_id']}/order_item_id/{order_item_id}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    def test_fetch_data_complete_order(self):
        """Проверка завершения заказа."""
        order_data = {
            "first_name": "John",
            "last_name": "Doe",
            "postal_zip": "12345",
            "address": "123 Main St",
            "city": "Springfield",
            "country": "USA"
        }
        url = (f"{BASE_URL}/order/complete-order/customer_id/{self.customer['customer_id']}/"
               f"first_name/{order_data['first_name']}/last_name/{order_data['last_name']}/"
               f"postal_zip/{order_data['postal_zip']}/address/{order_data['address']}/"
               f"city/{order_data['city']}/counry/{order_data['country']}")
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

if __name__ == "__main__":
    unittest.main()
