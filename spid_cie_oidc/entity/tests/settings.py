TA_SUB = "http://testserver/"
FA_METADATA = {
    "federation_entity": {
        "contacts": ["ops@localhost"],
        "federation_api_endpoint": f"{TA_SUB}/fetch",
        "homepage_uri": f"{TA_SUB}",
        "name": "example TA",
    }
}
TM_ISSUERS = {
    "https://www.spid.gov.it/certification/rp/public": [
        TA_SUB,
        "https://public.intermediary.spid.it",
    ],
    "https://www.spid.gov.it/certification/rp/private": [
        TA_SUB,
        "https://private.other.intermediary.it",
    ],
    "https://sgd.aa.it/onboarding": ["https://sgd.aa.it"],
}
FA_CONSTRAINTS = {"max_path_length": 1}

ta_conf_data = dict(
    sub=TA_SUB,
    metadata=FA_METADATA,
    constraints=FA_CONSTRAINTS,
    is_active=1,
    trust_marks_issuers=TM_ISSUERS,
)

rp_onboarding_data = dict(
    name = "RP Test",
    sub = "http://rp-test/",
    type = "openid_relying_party",
    
    metadata_policy = {"openid_relying_party": {"scopes": {"value": ["openid"]}}},
    is_active=True
)

TRUST_MARK_PAYLOAD = {
    "iss": "$.issuer_sub",
    "sub": "$.sub",
    "iat": 1579621160,
    "id": "https://www.spid.gov.it/certification/rp",
    "mark": "https://www.agid.gov.it/themes/custom/agid/logo.svg",
    "ref": "https://docs.italia.it/italia/spid/spid-regole-tecniche-oidc/it/stabile/index.html"
}

RP_PROFILE = {
    "name": "SPID Public SP",
    "profile_category": "openid_relying_party",
    "profile_id": "https://www.spid.gov.it/openid-federation/agreement/sp-public/",
    "trust_mark_template": TRUST_MARK_PAYLOAD
}

RP_METADATA = {
    "openid_relying_party": {
        "application_type": "web",
        "client_registration_types": ["automatic"],
        "client_name": "Name of this service called https://rp.example.it/spid",
        "contacts": ["ops@rp.example.it"],
        "grant_types": ["refresh_token", "authorization_code"],
        "jwks": {
            "kty": "RSA",
            "n": "1cE1PyQiBkmwO4TT30HGUwegdPZ9iKvuwQezUYOe8LqGol_6sUgxAf67_KbAeP1PMrmGH6d-AgNIT2Taa0OAtqyRUTLhG8rl7gT3_Jzwt2mOJu2JI4MfWcQxa-ZtzM8PPr7JUzWUzhHO7Nb1MfBm_fqB20cRcHOS_fvu3PqY-C-t33z3JYeDD_PsvSs2-WLlUiMDf9ILp0rVatF4GTPwvEp7VLCqCf1lLSLIxuuTVI0sc1j3xPbyv4MO_33fTmoAOVDmkUnhi2igLgw_tjc2-iu_4-r2qsKbotGiTu6y1RQrHc8xcrQmfqJ8FUwqAcpgQnlsekEHc6lWx9262Anobw",
            "e": "AQAB",
            "kid": "2C3zbeQjgx3jk-CHSqK3pLhdPeV9Fn5eSBPMNUp7vQk",
        },
        "redirect_uris": ["https://rp.example.it/spid/callback"],
        "response_types": ["code"],
        "subject_type": "pairwise",
    }
}
