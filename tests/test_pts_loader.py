"""Add parent directory to path"""
import os,sys,inspect
currentdir_loc = os.path.abspath(inspect.getfile(inspect.currentframe()))
currentdir = os.path.dirname(currentdir_loc)
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import unittest

from pts_loader import load

class TestLoader(unittest.TestCase):

	def test_load_pts_file(self):
		"""check that points are loaded correctly by 
		confirming a known value"""
		path = "sample_point_cloud.pts"
		points = load(path)
		expected_y_coord = 302.270092
		self.assertEqual(expected_y_coord, points[3][1])

if __name__ == '__main__':
	unittest.main()
