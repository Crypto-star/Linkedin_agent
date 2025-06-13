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
        "🎯 Base all advice on the user's actual industry and experience.\n"
        "🎯 Do NOT re-suggest certifications or skills already listed in the profile.\n\n"
    )

    if summary_context:
        prompt += f"Conversation so far (summary):\n{summary_context}\n\n"

    prompt += f"User's LinkedIn Profile Data:\n{profile_context}\n\n"
    if job_description:
        prompt += f"Target Job Description:\n{job_description}\n\n"

    # Intent logic
    if "roadmap" in user_intent.lower() or "become" in user_intent.lower():
        prompt += (
            "🎯 TASK: Generate a personalized career roadmap based on the user’s stated goal.\n"
            "Instructions:\n"
            "1. Summarize their current background once, avoiding repetition.\n"
            "2. Extract their target goal from the user input.\n"
            "3. Compare current profile vs. what's needed for that role.\n"
            "4. Create a gap analysis table: skills/experience present vs. missing.\n"
            "5. Lay out a short-, medium-, and long-term timeline to reach the goal.\n"
            "6. Recommend specific resources and steps to bridge the gaps.\n"
            "7. ⚠️ Do not hallucinate or fabricate any data or positions.\n"
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
