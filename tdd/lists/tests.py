from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
import re

from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    def remove_csrf(self, origin):
        csrf_regex = r'&lt;input[^&gt;]+csrfmiddlewaretoken[^&gt;]+&gt;'
        return re.sub(csrf_regex, '', html_code)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)

        self.assertIn('신규 작업 아이템', response.content.decode())
        expected_html = render_to_string('home.html', request=request)

        self.assertEqual(remove_csrf(response_decode), remove_csrf(expected_html))




class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.save()

        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.save()

        saved_item = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_save_item = save_items[0]
        second_save_item = save_items[1]
        self.assertEqual(first_save_item.text, '첫 번째 아이템')
        self.assertEqual(second_saved_item.text, '두 번째 아이템')