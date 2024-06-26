from django.test import TestCase
from ninja.testing import TestClient
from api.api import api


# Create a test client for interacting with the API
client = TestClient(api)


class CarTest(TestCase):

    n_cars = 5

    def setUp(self):
        """Sets up the test environment by creating 5 cars before each test."""

        for i in range(self.n_cars):
            client.post(
                "/",
                json={
                    "make": f"Make {i}",
                    "model": f"Model {i}",
                    "year": 2000 + i,
                    "color": f"Color {i}",
                    "price": 20000 + i,
                },
            )

    def test_create_car(self):
        """Tests creating a new car with valid data."""

        response = client.post(
            "/",
            json={
                "make": "Ford",
                "model": "Fiesta",
                "year": 2011,
                "color": "Panther Black",
                "price": 20000,
            },
        )
        assert response.status_code == 201
        assert response.json() == {
            "id": self.n_cars + 1,
            "make": "Ford",
            "model": "Fiesta",
            "year": 2011,
            "color": "Panther Black",
            "price": 20000.0,
        }

    def test_get_cars(self):
        """Tests retrieving a list of cars."""

        response = client.get("/")
        assert response.status_code == 200
        assert len(response.json()["items"]) == 5
        assert response.json() == {
            "count": 5,
            "items": [
                {
                    "id": i + 1,
                    "make": f"Make {i}",
                    "model": f"Model {i}",
                    "year": 2000 + i,
                    "color": f"Color {i}",
                    "price": 20000 + i,
                }
                for i in range(5)
            ],
        }

    def test_get_car(self):
        """Tests retrieving a single car by its ID."""

        response = client.get("/1")
        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "make": "Make 0",
            "model": "Model 0",
            "year": 2000,
            "color": "Color 0",
            "price": 20000.0,
        }

    def test_update_car(self):
        """Tests updating an existing car with new data."""

        response = client.put(
            "/1",
            json={
                "make": "Ford",
                "model": "Fiesta",
                "year": 2011,
                "color": "Panther Black",
                "price": 20000,
            },
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "make": "Ford",
            "model": "Fiesta",
            "year": 2011,
            "color": "Panther Black",
            "price": 20000.0,
        }

    def test_patch_car(self):
        """Tests partially updating an existing car with new data using PATCH."""

        response = client.patch(
            "/1",
            json={
                "make": "Ford",
                "model": "Fiesta",
            },
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "make": "Ford",
            "model": "Fiesta",
            "year": 2000,
            "color": "Color 0",
            "price": 20000.0,
        }

    def test_delete_car(self):
        """Tests deleting an existing car."""

        response = client.delete("/1")
        assert response.status_code == 200
        assert response.json() == {"success": True}
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {
            "count": 4,
            "items": [
                {
                    "id": i + 1,
                    "make": f"Make {i}",
                    "model": f"Model {i}",
                    "year": 2000 + i,
                    "color": f"Color {i}",
                    "price": 20000 + i,
                }
                for i in range(1, self.n_cars)
            ],
        }

    def test_create_car_with_missing_field(self):
        """Tests creating a car with a missing required field."""

        response = client.post("/", json={"model": "Fiesta", "year": 2011})
        assert response.status_code == 422

    def test_create_car_with_invalid_data(self):
        """Tests creating a car with invalid data type."""

        response = client.post(
            "/",
            json={
                "make": "Ford",
                "model": "Fiesta",
                "year": "invalid",
                "color": "Black",
                "price": 20000,
            },
        )
        assert response.status_code == 422
        assert response.json()["detail"]  # Check for error message in response

    def test_get_nonexistent_car(self):
        """Tests retrieving a non-existent car."""

        response = client.get("/100")
        assert response.status_code == 404

    def test_update_nonexistent_car(self):
        """Tests updating a non-existent car."""

        response = client.put(
            "/100",
            json={
                "make": "Ford",
                "model": "Fiesta",
                "year": 2011,
                "color": "Black",
                "price": 20000,
            },
        )
        assert response.status_code == 404

    def test_patch_nonexistent_car(self):
        """Tests partially updating a non-existent car."""

        response = client.patch("/100", json={"make": "Ford", "model": "Fiesta"})
        assert response.status_code == 404

    def test_delete_nonexistent_car(self):
        """Tests deleting a non-existent car."""

        response = client.delete("/100")
        assert response.status_code == 404

    def test_update_car_with_missing_all_fields(self):
        """Tests updating a car with an empty JSON object."""

        response = client.put("/1", json={})
        assert response.status_code == 422

    def test_update_car_with_missing_fields(self):
        """Tests updating a car with missing fields."""

        response = client.put("/1", json={"make": "Tesla"})
        assert response.status_code == 422

    def test_create_car_with_invalid_year(self):
        """Tests creating a car with an invalid year."""

        response = client.post(
            "/",
            json={
                "make": "Ford",
                "model": "Fiesta",
                "year": 1800,
                "color": "Black",
                "price": 20000,
            },
        )
        assert response.status_code == 422
        assert response.json()["detail"] == "Cars were not invented yet!"
