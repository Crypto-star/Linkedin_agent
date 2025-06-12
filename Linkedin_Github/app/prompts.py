# app/prompts.py
from typing import Optional

def build_profile_analysis_prompt(profile_context: str, job_description: Optional[str], summary_context: Optional[str], user_intent: str) -> str:
    prompt = (
        "You are a professional AI career assistant that provides detailed, realistic, and personalized career guidance based on the user's LinkedIn profile.\n"
        "⚠️ Only reference real profile data. Do not invent job titles, companies, or skills.\n\n"
    )

    if summary_context:
        prompt += f"Conversation so far (summary):\n{summary_context}\n\n"

    prompt += f"User's LinkedIn profile:\n{profile_context}\n\n"

    if job_description:
        prompt += f"Target Job Description:\n{job_description}\n\n"

    if "roadmap" in user_intent or "become" in user_intent:
        prompt += (
            "The user wants to grow their career. Based on their current profile, generate a personalized roadmap toward their stated goal.\n"
            "Include step-by-step progression, realistic suggestions, and highlight what they already have vs. what they need.\n"
        )
    elif "improve" in user_intent and "experience" in user_intent:
        prompt += (
            "Improve the user's work experience descriptions ONLY based on their real data.\n"
            "Do not invent any new roles or achievements. Just enhance wording.\n"
        )
    elif "what should i improve" in user_intent or "what do i need" in user_intent:
        prompt += (
            "Audit the profile section by section. Output a table like this:\n"
            "Section | Present | Quality | Suggestions\n"
            "--------|---------|---------|------------------------\n"
            "Summary | Yes     | Weak    | Add elevator pitch\n"
        )
    else:
        prompt += "Offer general career improvement suggestions based on this profile.\n"

    return prompt
