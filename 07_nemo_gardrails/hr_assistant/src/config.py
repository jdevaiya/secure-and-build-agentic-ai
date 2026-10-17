""" 
App-wide constants -models, prompts,and output-scan patterns 

"""
GROQ_MODELS = {
    "meta-llama/llama-prompt-guard-2-86m":"Llama prompt guard 2 80m for guardrails",
    "meta-llama/llama-prompt-guard-2-22m" : "Llama prompt guard 2 22m fast & cheap",
    "openai/gpt-oss-120b":"OpenAi OSS 120b - strong reasoning",
    "openai/gpt-oss-20b":"OpenAi OSS 20b - fast",
}

GUARD_MODEL_DEFAULT = "meta-llama/llama-prompt-guard-2-86m"
CHAT_MODEL_DEFAULT = "meta-llama/llama-prompt-guard-2-22m"

HR_SYSTEM_PROMPT = (
    "You are the HR Policy Assistant for acme corp"
    "Answer the employee's question using ONLY  the policy excerpts provided below."
    "Be concise , city the relevant policy section, and include specific number or rules where applicable."
    "If the answer is not covered in the employee to hr@jayendra.com . \n\n"
    "Policy Excerpts:\n{context}"
)

SENSITIVE_OUTPUT_PATTERNS = {
    "credential_leak": r"(?i)(password|passwd|secret|api[_\-]?key|token)\s*[:=]s*['\"]?\w{6,}",
    "ssn_in_output":r"\b\d{3}-\d{2}-\d{4}\b",
    "hardcoded_salary":r"(?i)\b(earns?|is paid|salary of)\s + \$[\d,]+\b",
}