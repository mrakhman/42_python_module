from book import Book
from recipe import Recipe
import unittest
from datetime import datetime

class TestRecipeAndBook(unittest.TestCase):
    def test_recipe(self):
        recipe = Recipe('tarte', 2, 40, ['dough', 'raspberries'], None, 'starter')

        # Test that recipe is instance of Recipe class
        self.assertIsInstance(recipe, Recipe)

        # Test that recipe has valid fields
        to_print = str(recipe)
        self.assertIn('Name: tarte', to_print)
        self.assertIn('Cooking time: 40', to_print)
        self.assertIn('Ingredients: dough, raspberries', to_print)

    
    def test_book(self):
        # Test create book
        cookbook = Book('new book')

        # Test that cookbook is instance of Book class
        self.assertIsInstance(cookbook, Book)

        # Test some cookbook fields
        self.assertEqual(cookbook.name, 'new book')
        self.assertLess(cookbook.creation_date, datetime.now())

        # Test that recipe that does not exist is not in cookbook
        invalid_recipe = cookbook.get_recipe_by_name('No name')
        self.assertIsNone(invalid_recipe)

        # Test adding recipe to the cookbook
        recipe = Recipe('tarte', 2, 40, ['dough', 'raspberries'], None, 'starter')
        cookbook.add_recipe(recipe)
        self.assertEqual('tarte', cookbook.get_recipe_by_name('tarte').name)

        # Test getting recipe by recipe type
        self.assertIsNone(cookbook.get_recipes_by_types('unknown type'))
        self.assertIsNone(cookbook.get_recipes_by_types('lunch'))
        self.assertEqual(cookbook.get_recipes_by_types('starter'), ['tarte'])


if __name__ == '__main__':
    unittest.main()
