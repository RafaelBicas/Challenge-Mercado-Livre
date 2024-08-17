class Json:
    def __init__(self, data):
        self.json_data = data.get('data', {}).get('attributes', {})

    def extract_relevant_content(self):
        attributes = self.json_data

        alert_contexts = []
        for result in attributes.get('crowdsourced_ids_results', []):
            alert = result.get('alert_context', [])
            alert_contexts.extend(alert)

        relevant_attributes = {
            "hash": {
                "sha1": attributes.get("sha1"),
                "sha256": attributes.get("sha256"),
                "md5": attributes.get("md5")
            },
            "Names": {
                "Original name": attributes.get("signature_info", {}).get("original name"),
                "Name variations": attributes.get("names")
            },
            "IoCs": {
                "Alerts context": alert_contexts
            },
            "Votes": {
            'malicious_votes': attributes.get('last_analysis_stats', {}).get('malicious'),
            'harmless_votes': attributes.get('last_analysis_stats', {}).get('harmless'),
            'suspicious_votes': attributes.get('last_analysis_stats', {}).get('suspicious')
            },
            "Malware informations": {
                'Popular threat classification': attributes.get('popular_threat_classification'),
            }

        }
        return relevant_attributes