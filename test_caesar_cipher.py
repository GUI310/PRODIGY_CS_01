import unittest
from caesar_cipher import encrypt, decrypt

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt('abc', 3), 'def')
        self.assertEqual(encrypt('ABC', 3), 'DEF')

    def test_decrypt(self):
        self.assertEqual(decrypt('def', 3), 'abc')
        self.assertEqual(decrypt('DEF', 3), 'ABC')

if __name__ == '__main__':
    unittest.main()
