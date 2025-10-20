#!/usr/bin/env python3
"""
Example Content Generation Examples
Demonstrates the Content Creation Agent with various scenarios.
"""

from content_agent import ContentCreationAgent, ContentRequest

def run_examples():
    """Run all examples to demonstrate agent capabilities"""
    
    # Initialize agent
    agent = ContentCreationAgent()
    
    print("CONTENT CREATION AGENT EXAMPLES")
    print("=" * 60)
    
    # Example 1: Blog Post
    example_blog()
    
    # Example 2: Social Media
    example_social_media()
    
    # Example 3: Newsletter
    example_newsletter()
    
    # Example 4: Video Script
    example_video_script()
    
    # Example 5: Email Campaign
    example_email_campaign()
    
    print("\n✨ All examples completed successfully!")
    print("Run 'python content_ui.py' to start the interactive interface.")

def example_blog():
    """Example: Professional blog post"""
    print("\n📄 EXAMPLE 1: PROFESSIONAL BLOG POST")
    print("-" * 50)
    
    agent = ContentCreationAgent()
    
    request = ContentRequest(
        topic="Benefits of DevOps for Startups",
        content_type="blog",
        target_audience="startup_founders",
        tone="professional"
    )
    
    try:
        variations, analysis = agent.generate_content(request)
        
        print(f"[OK] Generated {len(variations)} blog post variations")
        print(f"[INFO] Average word count: {sum(v.word_count for v in variations) // len(variations)}")
        
        # Show first variation details
        variation = variations[0]
        print(f"\nTitle: {variation.title}")
        print(f"Word Count: {variation.word_count}")
        print(f"Tags: {', '.join(variation.tags[:5])}")
        print(f"CTA: {variation.call_to_action}")
        
        print(f"\nContent Preview:")
        preview = variation.content[:250] + "..." if len(variation.content) > 250 else variation.content
        print(preview)
        
    except Exception as e:
        print(f"❌ Error: {e}")

def example_social_media():
    """Example: Social media post"""
    print("\n📱 EXAMPLE 2: SOCIAL MEDIA POST")
    print("-" * 40)
    
    agent = ContentCreationAgent()
    
    request = ContentRequest(
        topic="AI for Small Business",
        content_type="social_media",
        target_audience="general_audience",
        tone="conversational",
        platform="linkedin"
    )
    
    try:
        variations, analysis = agent.generate_content(request)
        
        print(f"✅ Generated {len(variations)} social media post variations")
        
        # Show each variation (social media posts are shorter)
        for i, variation in enumerate(variations, 1):
            print(f"\n📄 VARIATION {i}:")
            print(f"🎯 Title: {variation.title}")
            print(f"📏 Word Count: {variation.word_count}")
            print(f"📝 Content:")
            print(variation.content)
            print("-" * 30)
        
    except Exception as e:
        print(f"❌ Error: {e}")

def example_newsletter():
    """Example: Newsletter content"""
    print("\n📧 EXAMPLE 3: NEWSLETTER")
    print("-" * 35)
    
    agent = ContentCreationAgent()
    
    request = ContentRequest(
        topic="Digital Marketing Trends",
        content_type="newsletter",
        target_audience="marketing_professionals",
        tone="informative"
    )
    
    try:
        variations, analysis = agent.generate_content(request)
        
        print(f"✅ Generated {len(variations)} newsletter variations")
        
        variation = variations[0]
        print(f"\n📝 Title: {variation.title}")
        print(f"📏 Word Count: {variation.word_count}")
        print(f"📢 CTA: {variation.call_to_action}")
        
        print(f"\n📖 Newsletter Preview:")
        preview = variation.content[:300] + "..." if len(variation.content) > 300 else variation.content
        print(preview)
        
    except Exception as e:
        print(f"❌ Error: {e}")

def example_video_script():
    """Example: Video script"""
    print("\n🎬 EXAMPLE 4: VIDEO SCRIPT")
    print("-" * 35)
    
    agent = ContentCreationAgent()
    
    request = ContentRequest(
        topic="Remote Work Best Practices",
        content_type="video_script",
        target_audience="general_audience",
        tone="conversational",
        word_count=900
    )
    
    try:
        variations, analysis = agent.generate_content(request)
        
        print(f"✅ Generated {len(variations)} video script variations")
        
        variation = variations[0]
        print(f"\n📝 Title: {variation.title}")
        print(f"📏 Word Count: {variation.word_count}")
        print(f"🎬 Duration: ~{variation.word_count // 150} minutes")
        
        print(f"\n📖 Script Preview:")
        preview = variation.content[:400] + "..." if len(variation.content) > 400 else variation.content
        print(preview)
        
    except Exception as e:
        print(f"❌ Error: {e}")

def example_email_campaign():
    """Example: Email campaign"""
    print("\n📩 EXAMPLE 5: EMAIL CAMPAIGN")
    print("-" * 40)
    
    agent = ContentCreationAgent()
    
    request = ContentRequest(
        topic="Product Launch Strategy",
        content_type="email_campaign",
        target_audience="startup_founders",
        tone="persuasive"
    )
    
    try:
        variations, analysis = agent.generate_content(request)
        
        print(f"✅ Generated {len(variations)} email campaign variations")
        
        # Show subject lines and CTAs for all variations
        for i, variation in enumerate(variations, 1):
            print(f"\n📧 EMAIL VARIATION {i}:")
            
            # Extract subject line from content
            content_lines = variation.content.strip().split('\n')
            subject_line = ""
            for line in content_lines:
                if line.startswith("**Subject Line:**"):
                    subject_line = line.replace("**Subject Line:**", "").strip()
                    break
            
            print(f"📟 Subject: {subject_line}")
            print(f"📢 CTA: {variation.call_to_action}")
            print("-" * 30)
        
    except Exception as e:
        print(f"❌ Error: {e}")

def example_all_formats():
    """Single example showing all formats for the same topic"""
    print("\n🎭 EXAMPLE: ALL FORMATS - 'Customer Service Excellence'")
    print("=" * 65)
    
    agent = ContentCreationAgent()
    
    base_request = ContentRequest(
        topic="Customer Service Excellence",
        target_audience="general_audience",
        tone="professional",
        include_examples=True,
        include_seo=True
    )
    
    formats = [
        ("blog", "Blog Post"),
        ("social_media", "Social Media"),
        ("newsletter", "Newsletter"),
        ("video_script", "Video Script"),
        ("email_campaign", "Email Campaign")
    ]
    
    try:
        for format_code, format_name in formats:
            print(f"\n📄 {format_name.upper()}")
            print("-" * 30)
            
            request = ContentRequest(**base_request.__dict__)
            request.content_type = format_code
            
            variations, _ = agent.generate_content(request)
            variation = variations[0]
            
            print(f"🎯 Title: {variation.title}")
            print(f"📏 Word Count: {variation.word_count}")
            print(f"📝 Preview: {variation.content[:150]}...")
            print()
        
        print("✅ All formats generated successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def example_analysis():
    """Example showing detailed analysis"""
    print("\n📊 EXAMPLE: DETAILED ANALYSIS")
    print("-" * 40)
    
    agent = ContentCreationAgent()
    
    request = ContentRequest(
        topic="Sustainable Business Practices",
        content_type="blog",
        target_audience="startup_founders",
        tone="informative"
    )
    
    try:
        variations, analysis = agent.generate_content(request)
        
        print(f"✅ Generated analysis for {len(variations)} variations")
        print(f"📊 Analysis length: {len(analysis.split())} words")
        
        print(f"\n📖 Analysis Preview:")
        preview = analysis[:400] + "..." if len(analysis) > 400 else analysis
        print(preview)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_examples()
