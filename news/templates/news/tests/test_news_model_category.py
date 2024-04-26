from .test_news_base import NewsTestBase
from django.core.exceptions import ValidationError  # type: ignore


class NewsCategoryModelTest(NewsTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(name='Category Testing')
        return super().setUp()
    # Todos os meus testes ja vão ter uma categoria criada.

    def test_news_category_model_string_representation(self):
        self.assertEqual(str(self.category), self.category.name)
        # Este teste está verificando, se convertermos o objeto para
        # uma string(category), o resultado é a string esperada,
        # que neste caso é 'Category Testing'.

    def test_news_category_model_name_max_length_is_85_chars(self):
        self.category.name = 'A' * 86
        with self.assertRaises(ValidationError):
            self.category.full_clean()  # Aqui ocorre a validação.
