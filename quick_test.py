#!/usr/bin/env python3
"""
Quick test of Content Creation Agent
Simple test without Unicode characters for Windows compatibility.
"""

from content_agent import ContentCreationAgent, ContentRequest

def main():
    print("Content Creation Agent - Quick Test")
    print("=" * 50)
    
    # Initialize agent
    agent = ContentCreationAgent()
    
    # Test request
    request = ContentRequest(
        topic="Benefits of DevOps for Startups",
        content_type="blog",
        target_audience="startup_founders",
        tone="professional"
    )
    
    try:
        print("Generating content...")
        variations, analysis = agent.generate_content(request)
        
        print(f"[OK] Generated {len(variations)} variations")
        
        # Show first variation
        variation = variations[0]
        print(f"\nTitle: {variation.title}")
        print(f"Word Count: {variation.word_count}")
        print(f"CTA: {variation.call_to_action}")
        
        print(f"\nContent Preview:")
        preview = variation.content[:300] + "..." if len(variation.content) > 300 else variation.content
        print(preview)
        
        print("\n[OK] Test completed successfully!")
        
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
