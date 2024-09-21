from fastauth.common.security import decrypt, encrypt


def test_encrypt_and_decrypt_email(key: bytes):
    email = "alextraveylan@gmail.com"

    encrypted_email = encrypt(email, key)

    assert email == decrypt(encrypted_email, key)
