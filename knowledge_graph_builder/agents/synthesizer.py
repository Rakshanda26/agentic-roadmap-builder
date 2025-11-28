

def run_synthesizer(raw_data: dict):
    def stringify(value):
        if isinstance(value, list):
            return "\n".join([str(v) for v in value])
        return str(value)

    combined_text = "\n".join([stringify(v) for v in raw_data.values()])
    prompt = f"""
You are an expert career roadmap planner and education advisor.

When users ask about courses or preparation strategies, break down the roadmap into clear phases:

- Phase (e.g. Fundamentals, Specialization)
- Subtopics (e.g. Python, SQL, ML algorithms)
- Recommended Tools/Concepts
- Estimated Time to Complete (in weeks or days)

Output Format (Strict):
Phase -> Subtopic -> Tool or Detail (Time Estimate)
Use arrows only. No colons or lists.

Encourage commitment and clarity with timelines.
Ensure 12–20 roadmap paths that guide users progressively.
Focus on actionable, realistic, and structured steps.

Context:
{combined_text}
"""

    response = CLIENT.generate_completion(prompt=prompt)
    try:
        return response["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        return str(response)
