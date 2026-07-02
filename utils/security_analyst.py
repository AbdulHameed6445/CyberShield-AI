def generate_analysis(prediction, score, keywords, urls):

    threat_level = (
        "Critical" if score >= 80
        else "High" if score >= 50
        else "Medium" if score >= 20
        else "Low"
    )

    reasons = []

    if keywords:
        reasons.append(
            f"Detected {len(keywords)} suspicious keywords."
        )

    if urls:
        reasons.append(
            f"Found {len(urls)} URL(s) in the email."
        )

    if "password" in keywords:
        reasons.append(
            "Possible credential harvesting attempt detected."
        )

    if "verify" in keywords:
        reasons.append(
            "Verification request detected."
        )

    if "urgent" in keywords:
        reasons.append(
            "Urgency-based social engineering language detected."
        )

    recommendation = (
        "Do not click links, block sender, and report to the security team."
        if prediction == 1
        else
        "Email appears safe. Exercise normal caution."
    )

    return {
        "threat_level": threat_level,
        "reasons": reasons,
        "recommendation": recommendation
    }