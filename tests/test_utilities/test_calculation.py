from utilities import user, calculation


class TestCalculation:
    def setup_method(self):
        self.name = "John Doe Jr."
        self.email = "john123@doe.cc"
        self.password = "john1doe11212123"
        user.register(self.name, self.email, self.password)
        login = user.login(self.email, self.password)
        self._id = list(login)[0]
        self.user = {
            "id": self._id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

    def test_get_user_history_empty_state(self):
        empty_history = calculation.get_user_history(self._id)
        assert empty_history == []

    def test_get_user_history_non_empty_state(self):
        calculation.add_calculation(self._id, 10, 10)
        non_empty_history = calculation.get_user_history(self._id)
        assert non_empty_history != []

    def test_get_user_history_non_empty_state_bad_id(self):
        empty_history = calculation.get_user_history(121212121211212)
        assert empty_history == []

    def test_add_calculation(self):
        result = calculation.add_calculation(self._id, 10, 10)
        assert result == 1
