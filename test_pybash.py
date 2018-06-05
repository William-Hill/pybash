import unittest
import pybash
import os
import shutil


class test_PyBash(unittest.TestCase):

    def test_trim_string_from_head(self):
        output = pybash.trim_string_from_head("/usr/local/bin/esg_installarg_file")
        self.assertEqual(output, "esg_installarg_file")

    def test_trim_string_from_tail(self):
        output = pybash.trim_string_from_tail("8.0.33", ".")
        self.assertEqual(output, "8")

    def test_mkdir_p(self):
        pybash.mkdir_p("/tmp/test_dir")
        self.assertTrue(os.path.exists("/tmp/test_dir"))
        shutil.rmtree("/tmp/test_dir")


    def test_touch(self):
        pybash.touch("/tmp/test_file")
        self.assertTrue(os.path.exists("/tmp/test_file"))
        os.remove("/tmp/test_file")

    def test_pushd(self):
        current_dir = os.getcwd()

        with pybash.pushd("/Users"):
            self.assertEqual(os.getcwd(), "/Users")

        self.assertEqual(current_dir, os.getcwd())


    def test_symlink_force(self):
        pybash.touch("/tmp/test_file")
        pybash.symlink_force("/tmp/test_file", "/tmp/test_symlink")
        self.assertTrue(os.path.islink("/tmp/test_symlink"))


if __name__ == '__main__':
    unittest.main()
