from webauthn import generate_registration_options, options_to_json, verify_registration_response
from webauthn.helpers.structs import AuthenticatorSelectionCriteria, UserVerificationRequirement, RegistrationCredential

#https://github.com/duo-labs/py_webauthn/blob/master/examples/authentication.py
#https://duo.com/blog/going-passwordless-with-py-webauthn


challenge = []
options = []
id = "123"
def createFingerprint(name):
    global challenge
    global options
    global id
    info = generate_registration_options(rp_name="MFA Project", 
                                         rp_id="localhost.com", 
                                         user_name=name, 
                                         authenticator_selection=AuthenticatorSelectionCriteria(user_verification=UserVerificationRequirement.REQUIRED),
                                         #challenge=b"123"
                                         )
    #challenge[id] = info.challenge
    #info = generate_registration_options(rp_name="MFA Project", rp_id="localhost.com", user_name=name)
    options = options_to_json(info)
    print(options)
    return options

def verifyFingerprint(fingerInput):
    global challenge
    global id

    #credential = RegistrationCredential.parse_raw(fingerInput)
    verification = verify_registration_response(credential=fingerInput, expected_challenge=options.challenge, require_user_verification=True)
    assert verification.credential_id == "123"
    return
