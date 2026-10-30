class EthicalPolicyEngine:

    def make_decision(
        self,
        risk_result,
        intent_result,
        behavior_result
    ):

        risk_score = risk_result["overall_risk_score"]
        risk_level = risk_result["risk_level"]

        intent_level = intent_result["intent_level"]
        behavior_level = behavior_result["behavior_level"]
        repeated_harassment = behavior_result["repeated_harassment"]

        # High-risk cases
        if (
            risk_level == "HIGH"
            and intent_level == "HIGH"
            and repeated_harassment
        ):
            decision = "BLOCK"

            reason = (
                "High overall risk with high intent to harm "
                "and repeated harassment behavior detected."
            )

        # Medium-risk cases
        elif risk_level == "HIGH" or risk_level == "MEDIUM":

            decision = "FLAG"

            reason = (
                "Potentially harmful behavior detected. "
                "Human moderator review is recommended."
            )

        # Low-risk cases
        else:

            decision = "ALLOW"

            reason = (
                "No significant harassment risk detected."
            )

        return {
            "risk_score": risk_score,
            "risk_level": risk_level,
            "decision": decision,
            "reason": reason
        }