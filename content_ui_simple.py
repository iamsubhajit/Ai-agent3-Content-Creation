#!/usr/bin/env python3
"""
Simple Content Creation Agent UI (Windows Compatible)
"""

import os
from content_agent import ContentCreationAgent, ContentRequest

def main():
    print("Content Creation Agent")
    print("=" * 40)
    print("Generate high-quality content across multiple formats:")
    print("- Blog posts")
    print("- Social media posts") 
    print("- Newsletters")
    print("- Video scripts")
    print("- Email campaigns")
    print("=" * 40)
    
    agent = ContentCreationAgent()
    
    while True:
        print("\nEnter your content requirements:")
        print("(Press Enter with empty field to exit)")
        
        # Get inputs
        topic = input("Topic: ").strip()
        if not topic:
            break
            
        print("\nContent Types:")
        print("1. Blog Post")
        print("2. Social Media") 
        print("3. Newsletter")
        print("4. Video Script")
        print("5. Email Campaign")
        
        content_type_map = {
            "1": "blog",
            "2": "social_media", 
            "3": "newsletter",
            "4": "video_script",
            "5": "email_campaign"
        }
        
        while True:
            choice = input("Select content type (1-5): ").strip()
            if choice in content_type_map:
                content_type = content_type_map[choice]
                break
            print("Invalid choice. Please enter 1-5.")
        
        print("\nTarget Audiences:")
        print("1. Startup Founders")
        print("2. Tech Leads")
        print("3. Marketing Professionals") 
        print("4. General Audience")
        
        audience_map = {
            "1": "startup_founders",
            "2": "tech_leads",
            "3": "marketing_professionals", 
            "4": "general_audience"
        }
        
        while True:
            choice = input("Select audience (1-4): ").strip()
            if choice in audience_map:
                audience = audience_map[choice]
                break
            print("Invalid choice. Please enter 1-4.")
        
        print("\nContent Tones:")
        print("1. Professional")
        print("2. Conversational")
        print("3. Persuasive")
        print("4. Informative")
        print("5. Humorous")
        
        tone_map = {
            "1": "professional",
            "2": "conversational",
            "3": "persuasive", 
            "4": "informative",
            "5": "humorous"
        }
        
        while True:
            choice = input("Select tone (1-5): ").strip()
            if choice in tone_map:
                tone = tone_map[choice]
                break
            print("Invalid choice. Please enter 1-5.")
        
        # Optional parameters
        word_count = input("Word count (optional, press Enter for default): ").strip()
        word_count = int(word_count) if word_count else None
        
        platform = None
        if content_type == "social_media":
            print("\nSocial Media Platforms:")
            print("1. Twitter")
            print("2. LinkedIn") 
            print("3. Facebook")
            print("4. Instagram")
            print("5. General")
            
            platform_map = {
                "1": "twitter",
                "2": "linkedin",
                "3": "facebook", 
                "4": "instagram",
                "5": "general"
            }
            
            while True:
                choice = input("Select platform (1-5): ").strip()
                if choice in platform_map:
                    platform = platform_map[choice]
                    break
                print("Invalid choice. Please enter 1-5.")
        
        cta = input("Custom CTA (optional, press Enter to skip): ").strip()
        cta = cta if cta else None
        
        try:
            # Create request
            request = ContentRequest(
                topic=topic,
                content_type=content_type,
                target_audience=audience,
                tone=tone,
                word_count=word_count,
                platform=platform,
                call_to_action=cta
            )
            
            print("\nGenerating content...")
            variations, analysis = agent.generate_content(request)
            
            print(f"[OK] Generated {len(variations)} variations")
            
            # Show variations
            for i, variation in enumerate(variations, 1):
                print(f"\n--- VARIATION {i} ---")
                print(f"Title: {variation.title}")
                print(f"Word Count: {variation.word_count}")
                print(f"CTA: {variation.call_to_action}")
                
                # Show content preview
                preview = variation.content[:400] + "..." if len(variation.content) > 400 else variation.content
                print(f"\nContent Preview:\n{preview}")
                
                if input(f"\nShow full content for Variation {i}? (y/n): ").lower() == 'y':
                    print(f"\n--- FULL CONTENT VARIATION {i} ---")
                    print(variation.content)
            
            # Offer to save
            if input("\nSave content to file? (y/n)/: ").lower() == 'y':
                save_content(variations, request)
                
        except Exception as e:
            print(f"[ERROR] {e}")
        
        if input("\nGenerate more content? (y/n): ").lower() != 'y':
            break
    
    print("\nThank you for using Content Creation Agent!")

def save_content(variations, request):
    """Save content to files"""
    try:
        # Create directory
        content_dir = "generated_content"
        if not os.path.exists(content_dir):
            os.makedirs(content_dir)
        
        # Generate filename
        topic_clean = request.topic.lower().replace(" ", "_")[:20]
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save variations
        for i, variation in enumerate(variations, 1):
            filename = f"{content_dir}/{topic_clean}_variation_{i}_{timestamp}.txt"
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
        
        print(f"[OK] Content saved to {content_dir}/")
        
    except Exception as e:
        print(f"[ERROR] Failed to save: {e}")

if __name__ == "__main__":
    main()
