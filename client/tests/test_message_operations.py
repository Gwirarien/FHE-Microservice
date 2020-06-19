import numpy as np
import time
import pytest
from app.calculation.key_generator import KeyGenerator
from app.calculation.matrix_encryption import MatrixEncryption
from app.calculation.matrix_decryption import MatrixDecryption

class TestMessageOperations():

    def __suppress_warnings(self):
        import warnings
        warnings.simplefilter("ignore", category=PendingDeprecationWarning)
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def __set_up_key(self):
        key_gen = KeyGenerator()
        return key_gen.generate_secret_key()

    def __create_matrices(self, secret_key, message1, message2):
        encrypted_matrix_1 = MatrixEncryption().encrypt_message(secret_key, message1)
        encrypted_matrix_2 = MatrixEncryption().encrypt_message(secret_key, message2)
        return (encrypted_matrix_1, encrypted_matrix_2)

    def test_message_addition(self):
        self.__suppress_warnings()
        secret_key = self.__set_up_key()
        count = 0
        result = 0

        while result != 6:
            #Create matrices
            encrypted_matrix_1, encrypted_matrix_2 = self.__create_matrices(secret_key, 2.0, 4.0)
            sum_matrix = np.add(encrypted_matrix_1, encrypted_matrix_2)

            #Test method and check results
            result = MatrixDecryption().decrypt_message(secret_key, sum_matrix, False)
            count += 1
            if count > 100:
                break
        assert result, 6

    def test_message_subtraction(self):
        self.__suppress_warnings()
        secret_key = self.__set_up_key()
        count = 0
        result = 0

        while result != 2:
            #Create matrices
            encrypted_matrix_1, encrypted_matrix_2 = self.__create_matrices(secret_key, 4.0, 2.0)
            sum_matrix = np.subtract(encrypted_matrix_1, encrypted_matrix_2)

            #Test method and check results
            result = MatrixDecryption().decrypt_message(secret_key, sum_matrix, False)
            count += 1
            if count > 100:
                break
        assert result, 2