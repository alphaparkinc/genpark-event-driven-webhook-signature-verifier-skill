from client import EventDrivenWebhookSignatureVerifierClient

def main():
    client = EventDrivenWebhookSignatureVerifierClient()
    res = client.verify_webhook_signature('{"order_id": 8812}', 'v1,t=123,v1=abc', 'whsec_key')
    print('Webhook Signature Verifier: ' + res['verification_id'] + ' (Valid: ' + str(res['signature_valid']) + ')')
    print('Event Type: ' + res['parsed_event_type'] + ' | Replay Prevented: ' + str(res['replay_attack_prevented']))
    print('Audit Receipt URL: ' + res['signature_audit_receipt_url'])

if __name__ == '__main__':
    main()
