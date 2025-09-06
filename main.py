import google.generativeai as genai
import PIL.Image

class StyleAI:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def analyze_wardrobe(self, image_path):
        img = PIL.Image.open(image_path)
        prompt = "Analyze clothing items in this image. List type, color, patterns, style."
        response = self.model.generate_content([prompt, img])
        return response.text
    
    def generate_outfit_prompt(self, description):
        return f"Create photorealistic outfit: {description}. Model, urban background, casual style."

# Usage example
if __name__ == "__main__":
    ai = StyleAI("YOUR_API_KEY")
    analysis = ai.analyze_wardrobe("assets/wardrobe.jpg")
    print(analysis)
    prompt = ai.generate_outfit_prompt(analysis)
    print(prompt)Enteriimport google.generativeai as genai
import PIL.Image

class StyleAI:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def analyze_wardrobe(self, image_path):
        img = PIL.Image.open(image_path)
        prompt = "Analyze clothing items in this image. List type, color, patterns, style."
        response = self.model.generate_content([prompt, img])
        return response.text
    
    def generate_outfit_prompt(self, description):
        return f"Create photorealistic outfit: {description}. Model, urban background, casual style."

# Usage example
if __name__ == "__main__":
    ai = StyleAI("YOUR_API_KEY")
    analysis = ai.analyze_wardrobe("assets/wardrobe.jpg")
    print(analysis)
    prompt = ai.generate_outfit_prompt(analysis)
    print(prompt)Enter
