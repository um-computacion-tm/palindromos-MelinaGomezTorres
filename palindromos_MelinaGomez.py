import unittest

def is_palindrome(mystring):
    mystring = mystring.replace(" ", "")
    for indice in range(0, len(mystring)):
        if mystring[indice] != mystring[-(indice+1)]:
            return False
    return True

class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado, True)

    def test_b(self):
        resultado = is_palindrome('B')
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome('aa')
        self.assertEqual(resultado, True)

    def test_ab(self):
        resultado = is_palindrome('ab')
        self.assertEqual(resultado, False)

    def test_aCa(self):
        resultado = is_palindrome('aCa')
        self.assertEqual(resultado, True)

    def test_aCs(self):
        resultado = is_palindrome('aCs')
        self.assertEqual(resultado, False)

    def test_ABBA(self):
        resultado = is_palindrome('ABBA')
        self.assertEqual(resultado, True)

    def test_ABCA(self):
        resultado = is_palindrome('BACB')
        self.assertEqual(resultado, False)

    def test_ABCBA(self):
        resultado = is_palindrome('ABCBA')
        self.assertEqual(resultado, True)

    def test_ABCCBA(self):
        resultado = is_palindrome('ABCCBA')
        self.assertEqual(resultado, True)

    def test_ZBCCBA(self):
        resultado = is_palindrome('ZBCCBA')
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)

    def test_neuqueM(self):
        resultado = is_palindrome('neuqueM')
        self.assertEqual(resultado, False)

    def test_NeuqueN(self):
        resultado = is_palindrome('Neu queN')
        self.assertEqual(resultado, True)

    def test_reconocer(self):
        resultado = is_palindrome('reconocer')
        self.assertEqual(resultado, True)

    def test_oso(self):
        resultado = is_palindrome('oso')
        self.assertEqual(resultado, True)

    def test_sometemos(self):
        resultado = is_palindrome('sometemos')
        self.assertEqual(resultado, True)

    def test_1221(self):
        resultado = is_palindrome('1221')
        self.assertEqual(resultado, True)

    def test_1226(self):
        resultado = is_palindrome('1226')
        self.assertEqual(resultado, False)

    def test_12021(self):
        resultado = is_palindrome('120 21')
        self.assertEqual(resultado, True)

if __name__ == '__main__':


  unittest.main()
