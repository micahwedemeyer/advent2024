import unittest
from disk import Disk

def read_input(filename):
    with open(filename, 'r') as input:
        return input.read().strip()


class Tester(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_lines = read_input("input2.txt")
        self.disk = Disk(self.raw_lines)

    def test_parse_disk_map(self):
        # How it starts
        self.assertEqual([0,0,-1,-1,-1,1,1,1,-1,-1,-1,2,-1], self.disk.disk_slots[0:13])

        # How it ends
        self.assertEqual([8,8,8,8,9,9], self.disk.disk_slots[-6:])

        self.assertEqual(9, self.disk.max_id)

    def test_reorder_files(self):
        reordered = self.disk.reorder_files()

        # How it starts
        self.assertEqual([0,0,9,9,8,1,1,1,8,8,8,2], reordered[:12])

        # The inflection point
        self.assertEqual([5,6,6,-1], reordered[25:29])

    def test_checksum(self):
        reordered = self.disk.reorder_files()
        checksum = self.disk.checksum(reordered)
        self.assertEqual(1928, checksum)

    def test_find_file_block(self):
        block_9 = self.disk.find_file_block(9)
        block_2 = self.disk.find_file_block(2)
        self.assertEqual(range(40,42), block_9)
        self.assertEqual(range(11,12), block_2)

    def test_find_free_space(self):
        free_space_3 = self.disk.find_free_space(self.disk.disk_slots, 3)
        self.assertEqual(range(2,5), free_space_3)

        free_space_4 = self.disk.find_free_space(self.disk.disk_slots, 4)
        self.assertIsNone(free_space_4)

    def test_compact(self):
        compacted = self.disk.compact()
        print(compacted)


# unittest.main()



s = read_input("input.txt")
disk = Disk(s)
# reordered = disk.reorder_files()
# checksum = disk.checksum(reordered)

compacted = disk.compact()
checksum = disk.checksum(compacted)
print(checksum)
    