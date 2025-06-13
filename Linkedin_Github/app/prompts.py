from typing import Optional

def build_profile_analysis_prompt(profile_context: str, job_description: Optional[str], summary_context: Optional[str], user_intent: str) -> str:
    # Detect profile domain (tech vs non-tech)
    profile_lower = profile_context.lower()
    is_non_tech_profile = any(keyword in profile_lower for keyword in [
        "public speaking", "nonprofit", "advocate", "trainer", "leadership speaker", "keynote", "productivity", "coach", "hall of fame", "communication expert"
    ])

    prompt = (
        "You are an expert AI career coach helping users grow professionally using real LinkedIn profile data.\n"
        "⚠️ Strictly use the provided profile data. Do NOT fabricate details such as roles, degrees, or experience.\n"
        "🔁 Do NOT repeat any section or heading.\n"
        "🎯 Base all advice on the user's actual industry and experience. Suggest CTO if appropriate, else CIO/CSO/CPO for leadership/public-speaking backgrounds.\n"
        "🎯 Do NOT re-suggest certifications or skills already listed in the profile.\n\n"
    )

    if summary_context:
        prompt += f"Conversation so far (summary):\n{summary_context}\n\n"

    prompt += f"User's LinkedIn Profile Data:\n{profile_context}\n\n"
    if job_description:
        prompt += f"Target Job Description:\n{job_description}\n\n"

    # Intent logic
    if "roadmap" in user_intent.lower() or "become" in user_intent.lower():
        if is_non_tech_profile:
            # Leadership/CIO/CSO-focused
            prompt += (
                "🎯 TASK: Generate a personalized C-level transition roadmap for a user from a **non-tech background**.\n"
                "Instructions:\n"
                "1. List current leadership and management experience.\n"
                "2. Identify what technical and infrastructure gaps exist for transitioning into CTO/CIO/CSO roles.\n"
                "3. Create a clear comparison table of strengths vs. missing elements.\n"
                "4. Outline a timeline with short-, medium-, and long-term milestones.\n"
                "5. Recommend learning paths and resources to fill the gaps.\n"
                "6. ⚠️ Avoid repeating sections or suggesting what's already present.\n"
            )
        else:
            # Tech profile: follow standard roadmap
            prompt += (
                "🎯 TASK: Create a structured roadmap to help the user grow into a CTO role.\n"
                "Instructions:\n"
                "1. Briefly summarize current skills and roles (once only).\n"
                "2. Identify missing areas to reach CTO-level responsibility.\n"
                "3. Suggest realistic milestones and timeline: short-, medium-, and long-term.\n"
                "4. Recommend resources ONLY to fill actual gaps.\n"
                "5. ⚠️ Avoid any repetition in headings or sections.\n"
            )
    elif "improve" in user_intent.lower() and "experience" in user_intent.lower():
        prompt += (
            "Improve the user's work experience descriptions based strictly on their real experience. Do not invent achievements. Use professional, quantifiable language.\n"
        )
    elif "what should i improve" in user_intent.lower() or "what do i need" in user_intent.lower():
        prompt += (
            "Output a markdown table auditing each section of the profile:\n\n"
            "| Section | Present | Quality | Suggestions |\n"
            "|---------|---------|---------|-------------|\n"
        )
    else:
        prompt += "Offer professional advice based only on the current LinkedIn profile.\n"

    return prompt
