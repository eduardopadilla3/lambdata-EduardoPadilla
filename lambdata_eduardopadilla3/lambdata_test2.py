import unittest
# unittest supports a type of tests called unit tests
# A unit is the smallest cohesive piece of code we can test
# (usually something like a function or method)

# Other types of tests (you won't write now, just to be aware):
# - Integration: testing multiple pieces working together
# - End to end: testing a full "flow"/use case
# There are also manual/non-code tests that are common
# - User acceptance testing: show it to a user, get feedback
# - Manual running and checking


from oop_examples import Animal


class AnimalTests(unittest.TestCase):
    """Tests the instantiation and use of Animal."""
    def test_run(self):
        """Test that the run method outputs correctly."""
        animal = Animal('Cheetah', 96, 'carnivorous')
        self.assertEqual(animal.run(), 'Vroom!')


if __name__ == '__main__':
    # This conditional is for code that will be run
    # when we execute our file from the command line
    unittest.main()
