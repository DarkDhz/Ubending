from unittest import TestCase
from data.CategoryQueries import *
from data.CategoryQueries import _toJson


class TestCategoryQueries(TestCase):
    def test__to_json(self):
        allCategories = [{'id': 1, 'name': 'Cars'},
                         {'id': 2, 'name': 'Bikes'},
                         {'id': 3, 'name': 'Toys'},
                         {'id': 4, 'name': 'Home'},
                         {'id': 5, 'name': 'Sports'},
                         {'id': 6, 'name': 'Technology'},
                         {'id': 7, 'name': 'Videogames'},
                         {'id': 8, 'name': 'Clothes'},
                         {'id': 9, 'name': 'Plants'},
                         {'id': 10, 'name': 'Books & Music'},
                         {'id': 11, 'name': 'Cinema'},
                         {'id': 12, 'name': 'Pet adoption'}]
        categoryNames = ["Cars", "Bikes", "Toys", "Home", "Sports",
                      "Technology", "Videogames", "Clothes", "Plants",
                      "Books & Music", "Cinema", "Pet adoption"]
        for i in range(0,12):
            self.assertEqual(_toJson([i+1, categoryNames[i]]), allCategories[i])

    def test_get_all_categories(self):
        allCategories = [{'id': 1, 'name': 'Cars'},
                         {'id': 2, 'name': 'Bikes'},
                         {'id': 3, 'name': 'Toys'},
                         {'id': 4, 'name': 'Home'},
                         {'id': 5, 'name': 'Sports'},
                         {'id': 6, 'name': 'Technology'},
                         {'id': 7, 'name': 'Videogames'},
                         {'id': 8, 'name': 'Clothes'},
                         {'id': 9, 'name': 'Plants'},
                         {'id': 10, 'name': 'Books & Music'},
                         {'id': 11, 'name': 'Cinema'},
                         {'id': 12, 'name': 'Pet adoption'}]

        self.assertEqual(getAllCategories(), allCategories, "Error with getAllCategories().")

    def test_get_category_name_by_id(self):
        # TRY TO GET A CATEGORY FROM AN UNEXISTING CATEGORY ID
        self.assertEqual(getCategoryNameByID(0), 404)

        # TRY EVERY OTHER CATEGORY
        categoryNames = ["Cars", "Bikes", "Toys", "Home", "Sports",
                      "Technology", "Videogames", "Clothes", "Plants",
                      "Books & Music", "Cinema", "Pet adoption"]
        for i in range(0,12):
            self.assertEqual(getCategoryNameByID(i+1), categoryNames[i])

    def test__category_to_json(self):
        # DUPLICATE FUNCTION
        self.fail()

    def test_get_category_by_id(self):
        # TRY TO GET A CATEGORY FROM AN UNEXISTING CATEGORY ID
        self.assertEqual(getCategoryNameByID(0), 404)

        # TRY EVERY OTHER CATEGORY
        allCategories = [{'id': 1, 'name': 'Cars'},
                         {'id': 2, 'name': 'Bikes'},
                         {'id': 3, 'name': 'Toys'},
                         {'id': 4, 'name': 'Home'},
                         {'id': 5, 'name': 'Sports'},
                         {'id': 6, 'name': 'Technology'},
                         {'id': 7, 'name': 'Videogames'},
                         {'id': 8, 'name': 'Clothes'},
                         {'id': 9, 'name': 'Plants'},
                         {'id': 10, 'name': 'Books & Music'},
                         {'id': 11, 'name': 'Cinema'},
                         {'id': 12, 'name': 'Pet adoption'}]
        for i in range(0,12):
            self.assertEqual(getCategoryNameByID(i+1), allCategories[i]["name"])
