"""LGCS-204 local visual comparison gates; requires two user-supplied JPEG paths.
Set LGCS204_OLD and LGCS204_NEW to run; absent files cause explicit SKIP.
No image is published, overwritten, or edited by these tests.
"""
import math
import os
from pathlib import Path
import unittest
from image_comparison import compare,sha256

class LGCS204ImageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        old=os.environ.get('LGCS204_OLD')
        new=os.environ.get('LGCS204_NEW')
        if not old or not new or not Path(old).is_file() or not Path(new).is_file():
            raise unittest.SkipTest('Set LGCS204_OLD/LGCS204_NEW to two accessible originals')
        cls.old=old;cls.new=new
        cls.hash_before=(sha256(old),sha256(new))
        cls.metrics=compare(old,new)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls,'hash_before'):
            assert (sha256(cls.old),sha256(cls.new))==cls.hash_before, 'Source JPEG bytes changed'

    def test_01_two_originals_are_distinct(self):self.assertFalse(self.metrics['same_original_bytes'])
    def test_02_original_dimensions_match(self):self.assertEqual(self.metrics['before']['dimensions'],self.metrics['after']['dimensions'])
    def test_03_visible_change_positive(self):self.assertGreater(self.metrics['mean_abs_channel_difference'],0)
    def test_04_not_all_pixels_identical(self):self.assertLess(self.metrics['fraction_identical_rgb_pixels'],1)
    def test_05_central_more_changed_than_upper_left(self):
        r=self.metrics['regions'];self.assertGreater(r['central_mandala']['mean_abs_channel_difference'],r['upper_left_panel']['mean_abs_channel_difference'])
    def test_06_central_more_changed_than_upper_right(self):
        r=self.metrics['regions'];self.assertGreater(r['central_mandala']['mean_abs_channel_difference'],r['upper_right_panel']['mean_abs_channel_difference'])
    def test_07_background_below_central_change(self):
        r=self.metrics['regions'];self.assertLess(r['outer_background']['mean_abs_channel_difference'],r['central_mandala']['mean_abs_channel_difference'])
    def test_08_psnr_finite(self):self.assertTrue(math.isfinite(self.metrics['psnr_db']))
    def test_09_original_hashes_remain(self):self.assertEqual((sha256(self.old),sha256(self.new)),self.hash_before)
    def test_10_image_does_not_validate_exact_graph(self):self.assertIn('do not prove',self.metrics['interpretation_limit'])

if __name__=='__main__':unittest.main(verbosity=2)
