
import sys
import unittest
from unittest.mock import MagicMock, ANY

# Mock modules
sys.modules['google.generativeai'] = MagicMock()
sys.modules['langchain_google_genai'] = MagicMock()

# Import the code to test
from utils.bot import MathBot

class TestMathBot(unittest.TestCase):
    def test_system_prompt_content(self):
        """Test that the system prompt contains the required LaTeX and Notation instructions."""
        bot = MathBot(api_key="fake_key")
        
        # Mock LLM invoke
        bot.llm.invoke = MagicMock()
        bot.llm.invoke.return_value.content = "Mock response"
        
        # Call generate_response
        bot.generate_response("Test query")
        
        # Check arguments
        call_args = bot.llm.invoke.call_args
        messages = call_args[0][0] 
        system_message = messages[0].content
        
        # Assertions
        self.assertIn("Use LaTeX for all mathematical expressions", system_message)
        self.assertIn("$$ ... $$", system_message)
        self.assertIn("explicitly define the notation", system_message)

    def test_image_passing(self):
        """Test that image data is correctly passed to the LLM."""
        bot = MathBot(api_key="fake_key")
        bot.llm.invoke = MagicMock()
        bot.llm.invoke.return_value.content = "Mock response"
        
        fake_image_data = {"mime_type": "image/png", "data": "fakebase64"}
        
        bot.generate_response("Look at this image", image_data=fake_image_data)
        
        call_args = bot.llm.invoke.call_args
        messages = call_args[0][0]
        human_message_content = messages[1].content # System is 0, Human is 1
        
        # Expecting a list of content blocks
        self.assertIsInstance(human_message_content, list)
        self.assertEqual(human_message_content[0]['type'], 'text')
        self.assertEqual(human_message_content[1]['type'], 'image_url')
        self.assertIn("fakebase64", human_message_content[1]['image_url']['url'])

if __name__ == '__main__':
    unittest.main()
