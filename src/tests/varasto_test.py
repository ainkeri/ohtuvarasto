import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_tilavuus_negatiivinen(self):
        nega = Varasto(-3.0)
        self.assertAlmostEqual(nega.tilavuus, 0.0)
    
    def test_saldo_negatiivinen(self):
        nega = Varasto(10, alku_saldo = -3)
        self.assertAlmostEqual(nega.saldo, 0.0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)
    
    def test_ottamismaara_pienempi_kuin_nolla(self):
        self.varasto.lisaa_varastoon(2)

        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 0.0)
    
    def test_ei_voi_ottaa_liikaa(self):
        self.varasto.lisaa_varastoon(8)

        maara = self.varasto.ota_varastosta(10)
        
        self.assertAlmostEqual(maara, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_lisatty_maara_pienempaa_kuin_nolla(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0.0)
    
    def test_str(self):
        objekti = Varasto(10, alku_saldo=0)
        teksti = "saldo = 0, vielä tilaa 10"
        self.assertAlmostEqual(str(objekti), teksti)