#!/usr/bin/env python3
"""
Content Creation Agent User Interface
Provides an interactive command-line interface for creating content.
"""

import os
import sys
from typing import Dict, List
from content_agent import ContentCreationAgent, ContentRequest, ContentOutput

class ContentCreationUI:
    """Command-line interface for the Content Creation Agent"""
    
    def __init__(self):
        self.agent = ContentCreationAgent()
        self.running = True
        
    def run(self):
        """Main application loop"""
        self.display_welcome()
        
        while self.running:
            try:
                self.display_main_menu()
                choice = self.get_user_choice()
                self.handle_choice(choice)
            except KeyboardInterrupt:
                self.exit_gracefully()
            except Exception as e:
                self.handle_error(e)
    
    def display_welcome(self):
        """Display welcome message"""
        print("=" * 60)
        print("🚀 CONTENT CREATION AGENT")
        print("=" * 60)
        print("Generate high-quality content across multiple formats:")
        print("• Blog posts")
        print("• Social media posts")
        print("• Newsletters")
        print("• Video scripts")
        print("• Email campaigns")
        print("=" * 60)
        print()
    
    def display_main_menu(self):
        """Display main menu options"""
        print("\n📝 MAIN MENU")
        print("-" * 30)
        print("1. Create Content")
        print("2. Preview Content Types")
        print("3. Show Example")
        print("4. About")
        print("5. Exit")
        print("-" * 30)
    
    def get_user_choice(self) -> int:
        """Get user menu choice"""
        while True:
            try:
                choice = input("Enter your choice (1-5): ").strip()
                if choice in ['1', '2', '3', '4', '5']:
                    return int(choice)
                else:
                    print("❌ Invalid choice. Please enter 1-5.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
    
    def handle_choice(self, choice: int):
        """Handle user menu choice"""
        if choice == 1:
            self.create_content()
        elif choice == 2:
            self.preview_content_types()
        elif choice == 3:
            self.show_example()
        elif choice == 4:
            self.show_about()
        elif choice == 5:
            self.exit_gracefully()
    
    def create_content(self):
        """Interactive content creation process"""
        print("\n🎯 CONTENT CREATION")
        print("-" * 40)
        
        try:
            # Gather content requirements
            request = self.gather_content_requirements()
            if not request:
                return
            
            # Generate content
            print("\n⚙️ Generating content...")
            variations, analysis = self.agent.generate_content(request)
            
            # Display results
            self.display_results(variations, analysis, request)
            
            # Offer to save content
            self.offer_save_option(variations, analysis)
            
        except Exception as e:
            print(f"❌ Error creating content: {e}")
    
    def gather_content_requirements(self) -> ContentRequest:
        """Gather content requirements from user"""
        print("Please provide the following information:")
        print()
        
        # Topic
        topic = self.get_input("📌 Topic: ", "Enter the topic or subject for your content")
        if not topic:
            return None
        
        # Content type
        content_type = self.select_content_type()
        if not content_type:
            return None
        
        # Target audience
        audience = self.select_target_audience()
        
        # Tone
        tone = self.select_tone()
        
        # Additional options
        print("\n🔧 ADDITIONAL OPTIONS")
        print("-" * 25)
        
        word_count = self.get_word_count(content_type)
        platform = self.get_platform(content_type)
        cta = self.get_custom_cta()
        include_examples = self.get_boolean_input("Include examples and statistics? (y/n): ", True)
        include_seo = self.get_boolean_input("Include SEO optimization? (y/n): ", True)
        
        return ContentRequest(
            topic=topic,
            content_type=content_type,
            target_audience=audience,
            tone=tone,
            word_count=word_count,
            platform=platform,
            call_to_action=cta,
            include_examples=include_examples,
            include_seo=include_seo
        )
    
    def get_input(self, prompt: str, placeholder: str = "") -> str:
        """Get user input with validation"""
        while True:
            user_input = input(f"{prompt}").strip()
            if user_input:
                return user_input
            elif placeholder:
                print(f"💡 Example: {placeholder}")
            else:
                print("❌ This field is required.")
    
    def select_content_type(self) -> str:
        """Select content type"""
        print("\n📄 CONTENT TYPE")
        print("-" * 20)
        types = [
            ("1", "blog", "Blog Post"),
            ("2", "social_media", "Social Media Post"),
            ("3", "newsletter", "Newsletter"),
            ("4", "video_script", "Video Script"),
            ("5", "email_campaign", "Email Campaign")
        ]
        
        for num, code, name in types:
            print(f"{num}. {name}")
        
        while True:
            choice = input("\nSelect content type (1-5): ").strip()
            for num, code, name in types:
                if choice == num:
                    print(f"✅ Selected: {name}")
                    return code
            print("❌ Invalid choice. Please select 1-5.")
    
    def select_target_audience(self) -> str:
        """Select target audience"""
        print("\n👥 TARGET AUDIENCE")
        print("-" * 25)
        audiences = [
            ("1", "startup_founders", "Startup Founders"),
            ("2", "tech_leads", "Tech Leads"),
            ("3", "marketing_professionals", "Marketing Professionals"),
            ("4", "general_audience", "General Audience")
        ]
        
        for num, code, name in audiences:
            print(f"{num}. {name}")
        
        while True:
            choice = input("\nSelect target audience (1-4): ").strip()
            for num, code, name in audiences:
                if choice == num:
                    print(f"✅ Selected: {name}")
                    return code
            print("❌ Invalid choice. Please select 1-4.")
    
    def select_tone(self) -> str:
        """Select content tone"""
        print("\n🎭 CONTENT TONE")
        print("-" * 18)
        tones = [
            ("1", "professional", "Professional"),
            ("2", "conversational", "Conversational"),
            ("3", "persuasive", "Persuasive"),
            ("4", "informative", "Informative"),
            ("5", "humorous", "Humorous")
        ]
        
        for num, code, name in tones:
            print(f"{num}. {name}")
        
        while True:
            choice = input("\nSelect tone (1-5): ").strip()
            for num, code, name in tones:
                if choice == num:
                    print(f"✅ Selected: {name}")
                    return code
            print("❌ Invalid choice. Please select 1-5.")
    
    def get_word_count(self, content_type: str) -> int:
        """Get word count preference"""
        defaults = {
            'blog': 800,
            'social_media': 200,
            'newsletter': 600,
            'video_script': 1200,
            'email_campaign': 400
        }
        
        default = defaults.get(content_type, 500)
        
        while True:
            choice = input(f"Word count (default: {default}, or press Enter for default): ").strip()
            if not choice:
                return default
            
            try:
                count = int(choice)
                if count > 0:
                    return count
                else:
                    print("❌ Word count must be positive.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def get_platform(self, content_type: str) -> str:
        """Get social media platform for social content"""
        if content_type != 'social_media':
            return None
        
        print("\n📱 SOCIAL MEDIA PLATFORM")
        print("-" * 30)
        platforms = [
            ("1", "twitter", "Twitter"),
            ("2", "linkedin", "LinkedIn"),
            ("3", "facebook", "Facebook"),
            ("4", "instagram", "Instagram"),
            ("5", "general", "General")
        ]
        
        for num, code, name in platforms:
            print(f"{num}. {name}")
        
        while True:
            choice = input("\nSelect platform (1-5) or press Enter for general: ").strip()
            if not choice:
                return "general"
            
            for num, code, name in platforms:
                if choice == num:
                    print(f"✅ Selected: {name}")
                    return code
            print("❌ Invalid choice. Please select 1-5.")
    
    def get_custom_cta(self) -> str:
        """Get custom call-to-action"""
        choice = input("Custom call-to-action (optional, press Enter to skip): ").strip()
        return choice if choice else None
    
    def get_boolean_input(self, prompt: str, default: bool) -> bool:
        """Get boolean input from user"""
        default_text = "Y" if default else "N"
        while True:
            choice = input(f"{prompt}(default: {default_text}): ").strip().lower()
            if not choice:
                return default
            elif choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("❌ Please enter y/n or yes/no.")
    
    def display_results(self, variations: List[ContentOutput], analysis: str, request: ContentRequest):
        """Display generated content variations"""
        print("\n🎉 CONTENT GENERATED SUCCESSFULLY!")
        print("=" * 50)
        print(f"📊 Summary: {len(variations)} variations generated")
        print(f"📝 Average word count: {sum(v.word_count for v in variations) // len(variations)}")
        print("=" * 50)
        
        # Show each variation
        for i, variation in enumerate(variations, 1):
            print(f"\n📄 VARIATION {i}")
            print("-" * 30)
            print(f"🎯 Title: {variation.title}")
            print(f"📏 Word Count: {variation.word_count}")
            print(f"🔖 Tags: {', '.join(variation.tags[:5]) if variation.tags else 'None'}")
            
            if variation.call_to_action:
                print(f"📢 CTA: {variation.call_to_action}")
            
            # Show content preview
            content_preview = variation.content[:300] + "..." if len(variation.content) > 300 else variation.content
            print(f"\n📝 Preview:\n{content_preview}")
            
            # Ask if user wants to see full content
            if self.get_boolean_input("\nShow full content? (y/n): ", False):
                print(f"\n📄 FULL CONTENT - VARIATION {i}")
                print("=" * 40)
                print(variation.content)
                print("=" * 40)
        
。        # Show analysis
        if self.get_boolean_input("\nView detailed analysis? (y/n): ", False):
            print("\n📊 DETAILED ANALYSIS")
            print("=" * 40)
            print(analysis)
    
    def offer_save_option(self, variations: List[ContentOutput], analysis: str, request: ContentRequest):
        """Offer to save content to files"""
        if self.get_boolean_input("\nSave content to files? (y/n): ", False):
            try:
                self.save_content(variations, analysis, request)
                print("✅ Content saved successfully!")
            except Exception as e:
                print(f"❌ Error saving content: {e}")
    
    def save_content(self, variations: List[ContentOutput], analysis: str, request: ContentRequest):
        """Save content variations to files"""
        # Create content directory
        content_dir = "generated_content"
        if not os.path.exists(content_dir):
            os.makedirs(content_dir)
        
        # Generate filename prefix
        topic_prefix = request.topic.lower().replace(" ", "_").replace("_", "_")[:20]
        timestamp = self.get_timestamp()
        
        # Save each variation
        for i, variation in enumerate(variations, 1):
            filename = f"{content_dir}/{topic_prefix}_variation_{i}_{timestamp}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"CONTENT VARIATION {i}\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Topic: {request.topic}\n")
                f.write(f"Type: {request.content_type}\n")
                f.write(f"Audience: {request.target_audience}\n")
                f.write(f"Tone: {request.tone}\n")
                f.write(f"Word Count: {variation.word_count}\n")
                f.write(f"Title: {variation.title}\n\n")
                
                if variation.call_to_action:
                    f.write(f"Call-to-Action: {variation.call_to_action}\n\n")
                
                if variation.tags:
                    f.write(f"Tags: {', '.join(variation.tags)}\n\n")
                
                f.write("CONTENT:\n")
                f.write("-" * 20 + "\n")
                f.write(variation.content)
                f.write("\n" + "="*50 + "\n")
        
        # Save analysis
        analysis_filename = f"{content_dir}/{topic_prefix}_analysis_{timestamp}.txt"
        with open(analysis_filename, 'w', encoding='utf-8') as f:
            f.write("CONTENT ANALYSIS\n")
            f.write("=" * 50 + "\n\n")
            f.write(analysis)
    
    def preview_content_types(self):
        """Show preview of different content types"""
        print("\n📖 CONTENT TYPE PREVIEWS")
        print("=" * 50)
        
        examples = [
            ("Blog Post", "800 words", "Professional guide with section headings, examples, and actionable insights"),
            ("Social Media", "200 words", "Platform-optimized posts with hashtags and engagement hooks"),
            ("Newsletter", "600 words", "Formatted newsletter with introduction, main content, and subscriber engagement"),
            ("Video Script", "1200 words", "Complete script with hook, intro, main points, and call-to-action"),
            ("Email Campaign", "400 words", "Subject line, body content, and compelling call-to-action")
        ]
        
        for name, length, description in examples:
            print(f"\n📄 {name.upper()}")
            print(f"   📏 Length: {length}")
            print(f"   📝 Features: {description}")
    
    def show_example(self):
        """Show example content generation"""
        print("\n🔥 EXAMPLE: 'Benefits of DevOps for Startups'")
        print("=" * 60)
        
        # Create example request
        request = ContentRequest(
            topic="Benefits of DevOps for Startups",
            content_type="blog",
            target_audience="startup_founders",
            tone="professional",
            word_count=800
        )
        
        try:
            print("⚙️ Generating example content...")
            variations, analysis = self.agent.generate_content(request)
            
            print(f"\n📊 Generated {len(variations)} variations")
            print(f"📝 Average word count: {sum(v.word_count for v in variations) // len(variations)}")
            
            # Show first variation
            variation = variations[0]
            print(f"\n📄 EXAMPLE VARIATION")
            print("-" * 30)
            print(f"🎯 Title: {variation.title}")
            print(f"📏 Word Count: {variation.word_count}")
            print(f"📢 CTA: {variation.call_to_action}")
            
            # Show content preview
            content_preview = variation.content[:500] + "..." if len(variation.content) > 500 else variation.content
            print(f"\n📝 PREVIEW:\n{content_preview}")
            
            if self.get_boolean_input("\nView full example content? (y/n): ", False):
                print(f"\n📄 FULL EXAMPLE CONTENT")
                print("=" * 40)
                print(variation.content)
                print("=" * 40)
            
        except Exception as e:
            print(f"❌ Error generating example: {e}")
    
    def show_about(self):
        """Show about information"""
        print("\nℹ️ ABOUT CONTENT CREATION AGENT")
        print("=" * 50)
        print("A versatile AI-powered content generation system that creates")
        print("high-quality content across multiple formats:")
        print()
        print("🎯 Capabilities:")
        print("• Understand target audience and tone of voice")
        print("• Generate engaging, clear, and grammatically correct content")
        print("• Adapt content for different platforms and formats")
        print("• Provide catchy titles, headings, and CTAs")
        print("• Include examples, statistics, and relevant references")
        print("• Optimize content for readability and SEO")
        print()
        print("💡 Perfect for:")
        print("• Content creators and marketers")
        print("• Small business owners")
        print("• Startup founders")
        print("• Marketing agencies")
        print("• Anyone needing high-quality content quickly")
        print()
        print("🌟 Generate 3 variations of each content piece")
        print("📊 Includes detailed analysis and recommendations")
        print("=" * 50)
    
    def exit_gracefully(self):
        """Exit the application gracefully"""
        print("\n👋 Thank you for using the Content Creation Agent!")
        print("Happy creating! ✨")
        self.running = False
    
    def handle_error(self, error: Exception):
        """Handle application errors"""
        print(f"\n❌ An error occurred: {error}")
        print("The application will continue running. Please try again.")
    
    def get_timestamp(self) -> str:
        """Get timestamp string for file naming"""
        from datetime import datetime
        return datetime.now().strftime("%Y%m%d_%H%M%S")


def main():
    """Main entry point"""
    ui = ContentCreationUI()
    ui.run()


if __name__ == "__main__":
    main()
