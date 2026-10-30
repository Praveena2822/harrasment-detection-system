class RiskEngine:

    def calculate_risk(
        self,
        context_result,
        intent_result,
        severity_result,
        behavior_result
    ):

        # -----------------------------
        # 1. CONTEXT SCORE
        # -----------------------------
        if context_result["context_risk"] == "HIGH":
            context_score = 1.0

        elif context_result["context_risk"] == "MEDIUM":
            context_score = 0.5

        else:
            context_score = 0.0


        # -----------------------------
        # 2. INTENT SCORE
        # -----------------------------
        intent_score = intent_result["combined_intent_score"]


        # -----------------------------
        # 3. SEVERITY SCORE
        # -----------------------------
        severity_score = severity_result["severity_score"]


        # -----------------------------
        # 4. BEHAVIOR SCORE
        # -----------------------------
        if behavior_result["behavior_level"] == "HIGH":
            behavior_score = 1.0

        elif behavior_result["behavior_level"] == "MEDIUM":
            behavior_score = 0.5

        else:
            behavior_score = 0.0


        # -----------------------------
        # 5. OVERALL RISK SCORE
        # -----------------------------
        risk_score = (
            (context_score * 0.20) +
            (intent_score * 0.30) +
            (severity_score * 0.25) +
            (behavior_score * 0.25)
        )


        # -----------------------------
        # 6. RISK LEVEL
        # -----------------------------
        if risk_score >= 0.70:
            risk_level = "HIGH"

        # A single clearly aggressive message can score just below 0.40
        # because context/behavior history is initially empty. Use 0.35 as
        # the review threshold so strong text signals are not silently allowed.
        elif risk_score >= 0.35:
            risk_level = "MEDIUM"

        else:
            risk_level = "LOW"


        # -----------------------------
        # 7. RETURN RESULT
        # -----------------------------
        return {
            "context_score": round(context_score, 3),
            "intent_score": round(intent_score, 3),
            "severity_score": round(severity_score, 3),
            "behavior_score": round(behavior_score, 3),
            "overall_risk_score": round(risk_score, 3),
            "risk_level": risk_level
        }