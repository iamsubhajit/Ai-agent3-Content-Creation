#!/usr/bin/env python3
"""
Versatile Content Creation Agent
Generates high-quality content across multiple formats including blogs, 
social media posts, newsletters, video scripts, and email campaigns.
"""

import json
import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class ContentRequest:
    """Data class for content generation requests"""
    topic: str
    content_type: str
    target_audience: str
    tone: str
    word_count: Optional[int] = None
    platform: Optional[str] = None
    call_to_action: Optional[str] = None
    include_examples: bool = True
    include_seo: bool = True

@dataclass
class ContentOutput:
    """Data class for generated content"""
    title: str
    content: str
    headings: List[str]
    call_to_action: Optional[str] = None
    tags: List[str] = None
    word_count: int = 0
    readability_score: float = 0.0

class ContentCreationAgent:
    """
    A versatile AI agent for creating high-quality content across multiple formats.
    Supports blogs, social media, newsletters, video scripts, and email campaigns.
    """
    
    def __init__(self):
        self.content_types = {
            'blog': self._generate_blog_content,
            'social_media': self._generate_social_content,
            'newsletter': self._generate_newsletter_content,
            'video_script': self._generate_video_script,
            'email_campaign': self._generate_email_campaign
        }
        
        self.tone_templates = {
            'professional': {
                'style': 'Clear, authoritative, and industry-specific language',
                'emphasis': 'Expertise, credibility, and measurable results',
                'examples': 'Industry statistics, case studies, technical data'
            },
            'conversational': {
                'style': 'Friendly, accessible language with personal anecdotes',
                'emphasis': 'Relatability, story-telling, and personal experiences',
                'examples': 'Personal stories, relatable scenarios, everyday situations'
            },
            'persuasive': {
                'style': 'Compelling arguments with emotional and logical appeals',
                'emphasis': 'Benefits, urgency, and transformation',
                'examples': 'Before/after scenarios, success stories, compelling statistics'
            },
            'informative': {
                'style': 'Educational, clear explanations with structured information',
                'emphasis': 'Learning, understanding, and comprehensive coverage',
                'examples': 'Step-by-step guides, detailed explanations, comprehensive lists'
            },
            'humorous': {
                'style': 'Witty, light-hearted language with appropriate humor',
                'emphasis': 'Entertainment, engagement, and memorable content',
                'examples': 'Funny analogies, wordplay, entertaining scenarios'
            }
        }
        
        self.audience_profiles = {
            'startup_founders': {
                'pain_points': ['Rapid growth', 'Market validation', 'Resource constraints'],
                'interests': ['Growth strategies', 'Funding', 'Technology adoption'],
                'language': 'Business-focused, results-oriented'
            },
            'tech_leads': {
                'pain_points': ['Team management', 'Technical debt', 'Scalability'],
                'interests': ['Best practices', 'Team productivity', 'Architecture'],
                'language': 'Technical but accessible'
            },
            'marketing_professionals': {
                'pain_points': ['Lead generation', 'ROI measurement', 'Brand awareness'],
                'interests': ['Marketing trends', 'Campaign optimization', 'Customer acquisition'],
                'language': 'Strategy-focused, metrics-driven'
            },
            'general_audience': {
                'pain_points': ['Learning new concepts', 'Practical application'],
                'interests': ['Accessible information', 'Clear benefits'],
                'language': 'Simple, jargon-free'
            }
        }

    def generate_content(self, request: ContentRequest) -> Tuple[List[ContentOutput], str]:
        """
        Generate content based on the request parameters.
        Returns a tuple of (variations, analysis).
        """
        try:
            # Validate request
            if request.content_type not in self.content_types:
                raise ValueError(f"Unsupported content type: {request.content_type}")
            
            # Generate content variations
            variations = []
            
            # Generate 3 variations with different approaches
            for i in range(3):
                variation = self._generate_single_variation(request, i)
                variations.append(variation)
            
            # Generate analysis
            analysis = self._generate_content_analysis(request, variations)
            
            return variations, analysis
            
        except Exception as e:
            raise Exception(f"Content generation failed: {str(e)}")

    def _generate_single_variation(self, request: ContentRequest, variation_index: int) -> ContentOutput:
        """Generate a single variation of content"""
        return self.content_types[request.content_type](request, variation_index)

    def _generate_blog_content(self, request: ContentRequest, variation_index: int) -> ContentOutput:
        """Generate blog post content"""
        word_count = request.word_count or self._get_default_word_count('blog')
        
        # Generate title variations
        title_options = [
            f"The Ultimate Guide to {request.topic}",
            f"Why {request.topic} Matters More Than You Think",
            f"Transforming Your Business with {request.topic}: A Complete Guide",
            f"The Hidden Benefits of {request.topic} You Need to Know",
            f"Mastering {request.topic}: From Beginner to Expert"
        ]
        title = title_options[variation_index % len(title_options)]
        
        # Generate content structure
        content = self._build_blog_structure(request, title, word_count)
        
        # Extract headings
        headings = self._extract_headings(content)
        
        # Generate CTA
        cta = request.call_to_action or self._generate_default_cta(request)
        
        # Generate tags
        tags = self._generate_seo_tags(request.topic) if request.include_seo else []
        
        return ContentOutput(
            title=title,
            content=content,
            headings=headings,
            call_to_action=cta,
            tags=tags,
            word_count=self._count_words(content)
        )

    def _build_blog_structure(self, request: ContentRequest, title: str, word_count: int) -> str:
        """Build the complete blog post structure"""
        audience = self.audience_profiles.get(request.target_audience, self.audience_profiles['general_audience'])
        tone = self.tone_templates[request.tone]
        
        # Introduction
        intro = self._generate_blog_introduction(request.topic, audience, tone)
        
        # Main sections
        sections = [
            ("The Problem", self._generate_problem_section(request.topic, audience)),
            ("The Solution", self._generate_solution_section(request.topic, audience, tone)),
            ("Key Benefits", self._generate_benefits_section(request.topic, audience, tone)),
            ("Implementation", self._generate_implementation_section(request.topic, audience)),
            ("Real-World Examples", self._generate_examples_section(request.topic, tone))
        ]
        
        # Conclusion
        conclusion = self._generate_blog_conclusion(request.topic, audience, tone)
        
        # Combine all sections
        content_parts = [intro]
        for heading, section_content in sections:
            content_parts.append(f"## {heading}")
            content_parts.append(section_content)
            content_parts.append("")  # Add spacing
        
        content_parts.append("## Conclusion")
        content_parts.append(conclusion)
        
        return "\n".join(content_parts)

    def _generate_blog_introduction(self, topic: str, audience: dict, tone: dict) -> str:
        """Generate blog post introduction"""
        pain_points = ', '.join(audience['pain_points'][:2])
        
        intro_templates = [
            f"In today's fast-paced business environment, {topic} has emerged as a critical factor for success. Whether you're dealing with {pain_points} or seeking sustainable growth, understanding {topic} can be the game-changer your organization needs.",
            
            f"You've probably heard about {topic}, but do you truly understand its transformative potential? For {audience.get('interests', ['growth'])[0]} professionals, this isn't just another trend—it's a fundamental shift that can revolutionize how you operate.",
            
            f"The numbers don't lie: companies that successfully implement {topic} see remarkable improvements across multiple metrics. But here's what most people miss—it's not just about the technology or methodology, it's about the mindset shift that makes it all possible."
        ]
        
        return intro_templates[hash(topic) % len(intro_templates)]

    def _generate_problem_section(self, topic: str, audience: dict) -> str:
        """Generate problem identification section"""
        pain_points = audience['pain_points']
        
        return f"""Traditional approaches to {topic.replace('Benefits of ', '').replace(' for', '')} often fall short because they fail to address fundamental challenges:

- **{pain_points[0]}**: Most organizations struggle with this because they lack systematic approaches
- **Scalability Issues**: Rapid growth can quickly overwhelm unprepared teams
- **Resource Constraints**: Limited budgets and personnel create bottlenecks

These challenges aren't insurmountable, but they require a strategic, modern approach."""

    def _generate_solution_section(self, topic: str, audience: dict, tone: dict) -> str:
        """Generate solution presentation section"""
        return f"""The solution lies in adopting a comprehensive {topic.replace('Benefits of ', '').replace(' for', '')} strategy that addresses both immediate needs and long-term objectives.

**Core Principles:**

1. **Strategic Integration**: Seamlessly blend {topic.replace('Benefits of ', '').replace(' for', '')} into existing workflows
2. **Team Alignment**: Ensure all stakeholders understand the value and implementation process
3. **Continuous Improvement**: Build mechanisms for ongoing optimization and adaptation

**Implementation Framework:**

- Start with pilot projects to demonstrate quick wins
- Scale proven methodologies across teams and departments
- Measure progress using established KPIs and metrics
- Iterate and refine based on real-world feedback

{tone['examples']}: Companies implementing this approach typically see 30-40% improvements in key performance indicators within the first quarter."""

    def _generate_benefits_section(self, topic: str, audience: dict, tone: dict) -> str:
        """Generate benefits and ROI section"""
        return f"""**Immediate Benefits:**

- **Improved Efficiency**: Streamlined processes reduce time-to-market by 25-40%
- **Enhanced Quality**: Systematic approaches result in fewer errors and higher customer satisfaction
- **Cost Reduction**: Automation and optimization typically deliver 15-30% cost savings

**Long-term Advantages:**

- **Competitive Edge**: Organizations that master {topic.replace('Benefits of ', '').replace(' for', '')} consistently outperform competitors
- **Team Satisfaction**: Clear processes and continuous improvement boost employee engagement
- **Innovation Acceleration**: Structured frameworks enable faster experimentation and adaptation

**ROI Considerations:**

{tone['examples']} show that the average return on investment for {topic.replace('Benefits of ', '').replace(' for', '')} initiatives ranges from 200-400% within the first 18 months, making it one of the most valuable strategic investments available."""

    def _generate_implementation_section(self, topic: str, audience: dict) -> str:
        """Generate practical implementation guidance"""
        return f"""**Getting Started:**

1. **Assessment Phase** (Weeks 1-2)
   - Conduct comprehensive analysis of current state
   - Identify key stakeholders and decision makers
   - Define success metrics and timeline

2. **Planning Phase** (Weeks 3-4)
   - Develop detailed implementation roadmap
   - Allocate resources and assign responsibilities
   - Create communication and training plans

3. **Execution Phase** (Months 2-6)
   - Implement pilot programs with select teams
   - Monitor progress and adjust strategies
   - Scale successful approaches across organization

**Common Pitfalls to Avoid:**

- **Scope Creep**: Keep initial implementation focused on core objectives
- **Insufficient Training**: Invest in comprehensive team education
- **Inadequate Metrics**: Establish clear measurement systems from the start
- **Cultural Resistance**: Address change management proactively

**Success Metrics:**

- Process efficiency improvements
- Cost reduction percentages  
- Team satisfaction scores
- Customer satisfaction ratings"""

    def _generate_examples_section(self, topic: str, tone: dict) -> str:
        """Generate real-world examples and case studies"""
        return f"""**Case Study: Tech Startup Success Story**

A mid-stage startup implemented {topic.replace('Benefits of ', '').replace(' for', '')} as part of their growth strategy. Within six months, they achieved:

- 45% reduction in deployment time
- 60% fewer production incidents
- 35% improvement in customer satisfaction scores

**Industry Example: Enterprise Adoption**

A Fortune 500 company rolled out {topic.replace('Benefits of ', '').replace(' for', '')} across 200+ teams globally. Key results included:

- $2.3M in annual cost savings
- 50% faster feature delivery
- 80% reduction in manual processes

{tone['examples']} consistently demonstrate that companies embracing {topic.replace('Benefits of ', '').replace(' for', '')} outperform their peers across virtually every measurable dimension."""

    def _generate_blog_conclusion(self, topic: str, audience: dict, tone: dict) -> str:
        """Generate blog post conclusion"""
        return f"""The evidence is clear: {topic.replace('Benefits of ', '').replace(' for', '')} represents a fundamental shift in how successful organizations operate. Rather than being an optional enhancement, it's becoming a competitive necessity.

**Key Takeaways:**

- Strategic implementation delivers measurable ROI within months, not years
- Success depends on cultural adoption, not just technical implementation
- Continuous improvement and adaptation are essential for long-term success

The question isn't whether to embrace {topic.replace('Benefits of ', '').replace(' for', '')}, but how quickly you can get started. Organizations that delay implementation risk falling behind competitors who are already realizing the benefits.

**Ready to Transform Your Organization?**

The implementation journey begins with a single step—assessment of your current state and identification of immediate opportunities for improvement. With the right strategy and commitment, {topic.replace('Benefits of ', '').replace(' for', '')} can transform your organization from reactive to proactive, from inefficient to optimized, and from good to great."""

    def _generate_social_content(self, request: ContentRequest, variation_index: int) -> ContentOutput:
        """Generate social media content"""
        platform = request.platform or 'general'
        
        # Platform-specific character limits
        limits = {
            'twitter': 280,
            'linkedin': 700,
            'facebook': 500,
            'instagram': 2200,
            'general': 300
        }
        
        limit = limits.get(platform, limits['general'])
        
        # Generate variations based on platform and variation index
        if variation_index == 0:
            # Question-based engagement
            title = f"Quick Tip: {request.topic}"
            content = self._generate_question_post(request.topic, request.target_audience, limit)
        elif variation_index == 1:
            # Value-based content
            title = f"{request.topic} Explained"
            content = self._generate_value_post(request.topic, request.target_audience, limit)
        else:
            # Personal experience/story
            title = f"My Experience with {request.topic}"
            content = self._generate_story_post(request.topic, request.target_audience, limit)
        
        cta = self._generate_social_cta(request.topic, platform)
        tags = self._generate_social_tags(request.topic)
        
        return ContentOutput(
            title=title,
            content=content,
            headings=[],
            call_to_action=cta,
            tags=tags,
            word_count=len(content.split())
        )

    def _generate_communication_style(self, tone: str) -> dict:
        """Generate communication style based on tone"""
        return {
            'professional': 'authoritative, credible, data-driven',
            'conversational': 'friendly, accessible, personal',
            'persuasive': 'compelling, benefit-focused, action-oriented',
            'informative': 'educational, clear, comprehensive',
            'humorous': 'entertaining, engaging, memorable'
        }.get(tone, 'professional')

    def _get_default_word_count(self, content_type: str) -> int:
        """Get default word count for content type"""
        counts = {
            'blog': 800,
            'social_media': 200,
            'newsletter': 600,
            'video_script': 1200,
            'email_campaign': 400
        }
        return counts.get(content_type, 500)

    def _generate_communication_strategy(self, request: ContentRequest) -> str:
        """Generate communication strategy recommendations"""
        audience = self.audience_profiles.get(request.target_audience, self.audience_profiles['general_audience'])
        
        return f"""
**Communication Strategy for {request.target_audience.replace('_', ' ').title()}:**

- **Primary interests**: {', '.join(audience['interests'][:3])}
- **Pain points**: {', '.join(audience['pain_points'][:3])}
- **Communication style**: {audience['language']}
- **Content tone**: {self._generate_communication_style(request.tone)}
- **Engagement approach**: Focus on practical applications and measurable outcomes
"""

    def _generate_question_post(self, topic: str, audience: str, char_limit: int) -> str:
        """Generate social media post with question format"""
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        questions = [
            f"What's the biggest challenge you face with {topic_clean}? 🤔",
            f"Have you tried implementing {topic_clean} in your organization? What worked? What didn't?",
            f"If you could improve one thing about {topic_clean}, what would it be?",
            f"What advice would you give someone starting with {topic_clean}?"
        ]
        
        base_question = questions[hash(topic) % len(questions)]
        
        # Add context and hashtags
        context = f"\n\n💡 Share your thoughts below! Learning from each other's experiences helps us all grow."
        hashtags = self._generate_social_tags(topic)
        
        full_post = base_question + context + "\n\n" + hashtags
        return self._truncate_to_limit(full_post, char_limit)

    def _generate_value_post(self, topic: str, audience: str, char_limit: int) -> str:
        """Generate social media post with value-adding content"""
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        
        value_posts = [
            f"🚀 {topic_clean} Tip: Most organizations overlook this key principle...",
            f"💡 Quick {topic_clean} insight: The difference between success and failure often comes down to this one thing:",
            f"⚡ {topic_clean} Fact: Companies that do this correctly see 3x better results than those who don't",
            f"🎯 {topic_clean} Strategy: Stop focusing on tools, start focusing on this instead"
        ]
        
        base_content = value_posts[hash(topic) % len(value_posts)]
        explanation = "\n\nProper implementation requires understanding both the technical AND human elements. Many teams focus solely on the mechanics and miss the cultural transformation that drives success."
        
        hashtags = self._generate_social_tags(topic)
        
        full_post = base_content + explanation + "\n\n" + hashtags
        return self._truncate_to_limit(full_post, char_limit)

    def _generate_story_post(self, topic: str, audience: str, char_limit: int) -> str:
        """Generate social media post with personal story format"""
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        
        stories = [
            f"When we first started implementing {topic_clean}, we made every mistake in the book 😅",
            f"Two years ago, our team was struggling with {topic_clean}. Here's what changed everything...",
            f"I used to think {topic_clean} was just another business buzzword. Then I saw the results.",
            f"The most surprising thing about {topic_clean}? It wasn't what I expected at all..."
        ]
        
        base_story = stories[hash(topic) % len(stories)]
        lesson = "\n\nLesson learned: Success comes from consistent application of proven principles, not flashy tools or overnight transformations."
        
        hashtags = self._generate_social_tags(topic)
        
        full_post = base_story + lesson + "\n\n" + hashtags
        return self._truncate_to_limit(full_post, char_limit)

    def _generate_newsletter_content(self, request: ContentRequest, variation_index: int) -> ContentOutput:
        """Generate newsletter content"""
        word_count = request.word_count or 600
        
        title_templates = [
            f"Weekly Insights: {request.topic}",
            f"The {request.topic} Newsletter",
            f"Trending: {request.topic} Update",
            f"Deep Dive: {request.topic}"
        ]
        
        title = title_templates[variation_index % len(title_templates)]
        
        # Newsletter sections
        intro_section = self._generate_newsletter_intro(request.topic, request.target_audience)
        main_section = self._generate_newsletter_main(request.topic, request.target_audience, request.tone)
        featured_section = self._generate_newsletter_featured(request.topic)
        conclusion_section = self._generate_newsletter_conclusion(request.topic)
        
        content = f"""## Welcome to This Week's Issue

{intro_section}

## Featured Article: {request.topic}

{main_section}

## What's Trending

{featured_section}

## Closing Thoughts

{conclusion_section}

---
P.S. {self._generate_newsletter_ps(request.topic)}
"""
        
        headings = self._extract_headings(content)
        cta = "Subscribe to our weekly newsletter for more insights like this!"
        
        return ContentOutput(
            title=title,
            content=content,
            headings=headings,
            call_to_action=cta,
            tags=self._generate_seo_tags(request.topic),
            word_count=self._count_words(content)
        )

    def _generate_video_script(self, request: ContentRequest, variation_index: int) -> ContentOutput:
        """Generate video script content"""
        word_count = request.word_count or 1200
        
        duration_minutes = word_count // 150  # Average speaking pace
        
        title_templates = [
            f"How {request.topic} is Changing Everything",
            f"The Complete Guide to {request.topic}",
            f"{request.topic}: What You Need to Know",
            f"Why {request.topic} Matters More Than Ever"
        ]
        
        title = title_templates[variation_index % len(title_templates)]
        
        # Video script structure
        hook = self._generate_video_hook(request.topic, request.target_audience)
        intro = self._generate_video_intro(request.topic)
        main_points = self._generate_video_main_points(request.topic, request.target_audience)
        demonstration = self._generate_video_demonstration(request.topic)
        conclusion = self._generate_video_conclusion(request.topic)
        cta = self._generate_video_cta(request.topic)
        
        content = f"""# Video Script: {title}
**Duration: ~{duration_minutes} minutes**
**Target Audience: {request.target_audience.replace('_', ' ').title()}**

## Hook (0-15 seconds)
{hook}

## Introduction (15-45 seconds)
{intro}

## Main Content (45 seconds - {duration_minutes-1} minutes)
{main_points}

## Demonstration/Example ({duration_minutes-1}-{duration_minutes-0.5} minutes)
{demonstration}

## Conclusion ({duration_minutes-0.5}-{duration_minutes} minutes)
{conclusion}

## Call to Action (final 15 seconds)
{cta}

## Production Notes
- Include engaging visuals and graphics
- Add subtitles for accessibility
- Use energetic, clear delivery
- Maintain eye contact with camera
- Include relevant background music at low volume
"""

        headings = self._extract_headings(content)
        
        return ContentOutput(
            title=title,
            content=content,
            headings=headings,
            call_to_action=cta,
            tags=self._generate_seo_tags(request.topic),
            word_count=self._count_words(content)
        )

    def _generate_email_campaign(self, request: ContentRequest, variation_index: int) -> ContentOutput:
        """Generate email campaign content"""
        word_count = request.word_count or 400
        
        campaign_types = ['welcome', 'educational', 'promotional']
        campaign_type = campaign_types[variation_index % len(campaign_types)]
        
        title_templates = {
            'welcome': [f"Welcome to the {request.topic} Journey", f"Getting Started with {request.topic}"],
            'educational': [f"Understanding {request.topic}: A Complete Guide", f"The Science Behind {request.topic}"],
            'promotional': [f"Transform Your Business with {request.topic}", f"{request.topic}: The Game-Changer You Need"]
        }
        
        title_options = title_templates[campaign_type]
        title = title_options[variation_index % len(title_options)]
        
        # Create email content
        subject_line = self._generate_email_subject(request.topic, campaign_type)
        body = self._generate_email_body(request.topic, campaign_type, request.target_audience)
        footer = self._generate_email_footer(request.topic)
        
        content = f"""**Subject Line:** {subject_line}

---

**Email Body:**

{body}

---

**Footer:**
{footer}
"""
        
        headings = self._extract_headings(content)
        
        return ContentOutput(
            title=title,
            content=content,
            headings=headings,
            call_to_action=self._generate_email_cta(campaign_type),
            tags=self._generate_seo_tags(request.topic),
            word_count=self._count_words(content)
        )

    def _generate_content_analysis(self, request: ContentRequest, variations: List[ContentOutput]) -> str:
        """Generate analysis and recommendations for the content variations"""
        avg_word_count = sum(v.word_count for v in variations) / len(variations)
        
        communication_strategy = self._generate_communication_strategy(request)
        
        analysis = f"""
# Content Generation Analysis

## Overview
- **Topic**: {request.topic}
- **Content Type**: {request.content_type}
- **Target Audience**: {request.target_audience.replace('_', ' ').title()}
- **Tone**: {request.tone.title()}
- **Average Word Count**: {avg_word_count:.0f} words

## Content Variations Summary
"""
        
        for i, variation in enumerate(variations, 1):
            analysis += f"\n### Variation {i}: {variation.title}\n"
            analysis += f"- **Word Count**: {variation.word_count}\n"
            analysis += f"- **Call to Action**: {variation.call_to_action}\n"
            analysis += f"- **Key Tags**: {', '.join(variation.tags[:5]) if variation.tags else 'None'}\n"
        
        analysis += communication_strategy
        
        analysis += f"""
## Recommendations

1. **Best for Professional Use**: Variation 2 typically works best for B2B audiences
2. **Highest Engagement**: Variation 1 tends to generate more social shares
3. **SEO Optimization**: Include targeted keywords naturally throughout content
4. **Platform Adaptation**: Modify tone and length based on target platform

## Next Steps

1. Review all variations and select the best fit for your objectives
2. Customize selected content with your brand voice and specific examples
3. Add relevant images, links, and formatting for optimal presentation
4. Schedule publication timing for maximum audience engagement
"""
        
        return analysis

    # Helper methods for content generation
    def _truncate_to_limit(self, text: str, char_limit: int) -> str:
        """Truncate text to character limit while preserving words"""
        if len(text) <= char_limit:
            return text
        
        truncated = text[:char_limit]
        last_space = truncated.rfind(' ')
        if last_space > char_limit * 0.8:  # Don't truncate too harshly
            truncated = truncated[:last_space]
        
        return truncated + "..."

    def _extract_headings(self, content: str) -> List[str]:
        """Extract headings from markdown content"""
        import re
        headings = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
        return headings

    def _count_words(self, text: str) -> int:
        """Count words in text"""
        return len(text.split())

    def _generate_seo_tags(self, topic: str) -> List[str]:
        """Generate SEO-optimized tags"""
        topic_words = topic.lower().split()
        base_tags = ['technology', 'business', 'strategy', 'innovation', 'growth']
        
        # Add topic-specific tags
        specific_tags = []
        for word in topic_words:
            if word not in ['of', 'for', 'the', 'and', 'a', 'an']:
                specific_tags.append(word)
        
        return list(set(base_tags + specific_tags))[:10]

    def _generate_social_tags(self, topic: str) -> str:
        """Generate social media hashtags"""
        tags = self._generate_seo_tags(topic)
        hashtags = [f"#{tag}" for tag in tags[:5]]
        return " ".join(hashtags)

    def _generate_default_cta(self, request: ContentRequest) -> str:
        """Generate default call-to-action"""
        topic_clean = request.topic.replace('Benefits of ', '').replace(' for', '')
        
        ctas = [
            f"Ready to implement {topic_clean} in your organization? Start with our free assessment tool.",
            f"Want to learn more about {topic_clean}? Download our comprehensive guide today.",
            f"Start your {topic_clean} journey today. Get personalized recommendations for your team.",
            f"Transform your business with {topic_clean}. Book a consultation to get started."
        ]
        
        return ctas[hash(request.topic) % len(ctas)]

    def _generate_social_cta(self, topic: str, platform: str) -> str:
        """Generate social media call-to-action"""
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        
        if platform == 'linkedin':
            return f"Looking to implement {topic_clean}? Let's connect and discuss how we can help your organization succeed."
        else:
            return f"What's your experience with {topic_clean}? Share your thoughts in the comments! 💬"

    # Newsletter helper methods
    def _generate_newsletter_intro(self, topic: str, audience: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        return f"In this week's newsletter, we're diving deep into {topic_clean} and its impact on modern business. Whether you're just getting started or looking to optimize your current approach, this edition has something for everyone."

    def _generate_newsletter_main(self, topic: str, audience: str, tone: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        return f"""**Understanding {topic_clean}**

Recent industry data shows that organizations embracing {topic_clean} principles see significant improvements across multiple metrics:

• 35% faster project completion times
• 40% reduction in manual errors  
• 60% improvement in team collaboration

But here's what's interesting: successful implementation isn't just about following processes—it's about creating a culture of continuous improvement.

**Key Implementation Strategies:**

1. **Start Small**: Begin with pilot projects in select teams
2. **Measure Everything**: Establish clear KPIs before implementation
3. **Communicate Value**: Ensure all stakeholders understand the benefits
4. **Iterate Quickly**: Use feedback loops to refine approaches

The companies seeing the best results aren't those with the most sophisticated tools—they're those with the clearest understanding of what they're trying to achieve."""

    def _generate_newsletter_featured(self, topic: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        return f"""**Industry Spotlight**: This week, we're featuring how TechCorp successfully scaled {topic_clean} across 500+ employees in just 4 months. Their secret? Focusing on human elements before technical implementation.

**Quick Question**: What's been your biggest challenge with {topic_clean} implementation? Reply to this email and we'll feature the best insights in next week's edition.

**Resource Spotlight**: Check out our updated {topic_clean} toolkit with 15 proven templates and frameworks."""

    def _generate_newsletter_conclusion(self, topic: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        return f"""The future belongs to organizations that can adapt quickly and continuously improve. {topic_clean} provides the framework for exactly that kind of transformation.

Whether you're just beginning your journey or looking to take your current implementation to the next level, focus on the fundamentals: clear strategy, proper communication, and consistent execution.

What questions do you have about {topic_clean}? We'd love to hear from you—just reply to this email."""

    def _generate_newsletter_ps(self, topic: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        return f"Don't forget: {topic_clean} is a marathon, not a sprint. Take time to celebrate small wins along the way! 🎉"

    # Video script helper methods  
    def _generate_video_hook(self, topic: str, audience: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        return f"What if I told you that {topic_clean} could transform your business in ways you never imagined? Today, I'm going to share the exact framework that's helped dozens of companies achieve remarkable results."

    def _generate_video_intro(self, topic: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        return f"Hi everyone! I'm excited to talk about {topic_clean} today because I've seen firsthand how it can completely change how organizations operate. In the next few minutes, I'll walk you through what {topic_clean} really means, why it matters, and most importantly, how you can implement it successfully."

    def _generate_video_main_points(self, topic: str, audience: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        return f"""**Point 1: Understanding the Fundamentals**
{topic_clean} isn't just about processes—it's about mindset. The most successful implementations start with understanding WHY before jumping into HOW.

**Point 2: Common Implementation Challenges**  
Most organizations struggle with three things: resistance to change, unclear objectives, and insufficient training. Here's how to avoid these pitfalls...

[your_name] shares anecdotal evidence or real-world case study

**Point 3: Building Sustainable Success**
Sustainable {topic_clean} implementation requires ongoing commitment and continuous learning. It's not a one-time project—it's an ongoing journey."""

    def _generate_video_demonstration(self, topic: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        return f"Let me show you exactly how this works in practice. [Insert demonstration of {topic_clean} principles in action] This real-world example shows the difference between theoretical knowledge and practical application."

    def _generate_video_conclusion(self, topic: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        return f"""{topic_clean} isn't just another business trend—it's a fundamental shift in how successful organizations operate. The companies embracing these principles today are building sustainable competitive advantages that will serve them for years to come.

Remember: Success comes from consistent application of proven principles, not perfection on day one."""

    def _generate_video_cta(self, topic: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        return f"If you found this helpful, please like and subscribe for more content like this. And if you're ready to start your {topic_clean} journey, check out the link in the description for our complete starter kit. Thanks for watching!"

    # Email campaign helper methods
    def _generate_email_subject(self, topic: str, campaign_type: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        
        subjects = {
            'welcome': [
                f"Welcome to the {topic_clean} Success Hub! 🚀",
                f"Getting Started with {topic_clean}: Your Journey Begins Now"
            ],
            'educational': [
                f"The Complete Guide to {topic_clean} (Free)",
                f"Understanding {topic_clean}: What Everyone Gets Wrong"
            ],
            'promotional': [
                f"Transform Your Business with {topic_clean}",
                f"{topic_clean}: The Secret Your Competitors Don't Know"
            ]
        }
        
        return subjects[campaign_type][hash(topic) % len(subjects[campaign_type])]

    def _generate_email_body(self, topic: str, campaign_type: str, audience: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        
        if campaign_type == 'welcome':
            return f"""Hi there!

Welcome to our community of {topic_clean} practitioners! 🎉

You've just joined thousands of professionals who are transforming their organizations through strategic {topic_clean} implementation.

Here's what you can expect:

✓ Weekly insights and best practices
✓ Exclusive resources and templates  
✓ Direct access to our expert team
✓ Member-only webinars and workshops

**Getting Started:**
1. Complete your profile in our member portal
2. Download your welcome package
3. Join our community discussion forum

Ready to dive in? Click below to access your starter resources!

Best regards,
The Team"""

        elif campaign_type == 'educational':
            return f"""Hi,

I wanted to share something important about {topic_clean} that most people miss.

After analyzing hundreds of implementations, I've noticed a pattern:

The successful companies aren't those with the biggest budgets or the latest tools—they're the ones that understand the fundamental principles behind {topic_clean}.

**What Sets Successful Organizations Apart:**

1. They start with clear objectives, not trendy tools
2. They focus on cultural adoption first, technical implementation second  
3. They measure progress continuously and adjust quickly
4. They invest in training and ongoing support

**The 80/20 Rule of {topic_clean}:**
80% of your results come from 20% of the core principles. Master these fundamentals, and everything else becomes much easier.

Want to learn the specific 20% that delivers massive results? 

Download our comprehensive guide (completely free) and discover the framework that's helped organizations achieve remarkable transformation.

To your success,
[Your Name]"""

        else:  # promotional
            return f"""Hi [Name],

What if I told you that in 90 days, you could transform how your organization operates with {topic_clean}?

I know that seems ambitious, but I've seen it happen dozens of times.

The secret isn't working harder—it's working smarter with proven frameworks that thousands of successful organizations use.

**Here's What You Get:**

✅ Our complete {topic_clean} implementation toolkit
✅ Access to our exclusive member community  
✅ Personalized consultation with our experts
✅ Ongoing support during your transformation

**Special Offer (Limited Time):**
Normally $997, but as a valued subscriber, you can access everything for just $297.

This includes everything you need to get started immediately:
- 25 proven templates and frameworks
- Video training series (5+ hours of content)
- Monthly group coaching calls
- Direct email support

**But this offer expires at midnight tonight.**

That's because we believe in results, not indefinite deliberation. If you're ready to transform your organization with {topic_clean}, now's the time to act.

Click below to secure your spot before it's too late.

Best regards,
[Your Name]

P.S. Questions? Just reply to this email—I personally read every response."""

    def _generate_email_footer(self, topic: str) -> str:
        topic_clean = topic.replace('Benefits of ', '').replace(' for', '')
        return f"""---
**Need help implementing {topic_clean}?** 
Book a free consultation: [your-website.com/consultation]

**Connect with us:**
Blog | LinkedIn | Twitter | YouTube

© 2024 Your Company Name. All rights reserved.
You received this email because you subscribed to our newsletter.
Unsubscribe | Update preferences"""

    def _generate_email_cta(self, campaign_type: str) -> str:
        ctas = {
            'welcome': "Access Your Starter Resources →",
            'educational': "Download Free Guide →", 
            'promotional': "Claim Your Spot Now →"
        }
        return ctas.get(campaign_type, "Learn More →")


if __name__ == "__main__":
    # Example usage
    agent = ContentCreationAgent()
    
    # Example request
    request = ContentRequest(
        topic="Benefits of DevOps for Startups",
        content_type="blog",
        target_audience="startup_founders",
        tone="professional"
    )
    
    try:
        variations, analysis = agent.generate_content(request)
        
        print("=== CONTENT GENERATION SUCCESSFUL ===")
        print(f"Generated {len(variations)} variations")
        print(f"Analysis: {len(analysis.split())} words")
        
        # Display first variation
        print("\n=== VARIATION 1 ===")
        print(f"Title: {variations[0].title}")
        print(f"Word Count: {variations[0].word_count}")
        print(f"CTA: {variations[0].call_to_action}")
        print(f"Tags: {', '.join(variations[0].tags[:5])}")
        
    except Exception as e:
        print(f"Error: {e}")
