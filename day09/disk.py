class Disk:
    def __init__(self, disk_map):
        self.raw_map = disk_map
        self.int_map = [int(c) for c in self.raw_map]
        self.disk_slots = self._parse_disk_map(self.int_map)

    def _parse_disk_map(self, int_map):
        # If it's not an even-length, add a 0 at the end to indicate "zero free space after this"
        int_map_copy = int_map.copy()
        if (divmod(len(int_map_copy), 2)[1] != 0):
            int_map_copy.append(0)

        pairs = list(zip(int_map_copy[::2], int_map_copy[1::2]))

        file_id = 0
        disk_slots = []
        for file_size, free_space in pairs:
            disk_slots += [file_id for j in range(file_size)]
            disk_slots += [-1 for j in range(free_space)]
            file_id += 1


        self.max_id = file_id - 1
        return disk_slots

    def reorder_files(self):
        disk_slot_copy = self.disk_slots.copy()
        free_idx = 0
        block_idx = len(disk_slot_copy) - 1

        while free_idx < block_idx:
            # Find the next free slot
            free_idx = disk_slot_copy.index(-1)

            # Find the next file block (from the back)
            found = False
            while not found and block_idx >= 0:
                if disk_slot_copy[block_idx] != -1:
                    found = True
                else:
                    block_idx -= 1

            if free_idx < block_idx:
                disk_slot_copy[free_idx] = disk_slot_copy[block_idx]
                disk_slot_copy[block_idx] = -1

        return disk_slot_copy

    def checksum(self, reordered):
        return sum([reordered[i] * i for i in range(len(reordered)) if reordered[i] != -1])

    def find_file_block(self, file_id):
        indexes = [i for i, val in enumerate(self.disk_slots) if val == file_id]
        if indexes == []:
            return None
        return range(indexes[0], indexes[-1] + 1)

    def find_free_space(self, disk_slots, file_size):
        for i in range(len(disk_slots)):
            if disk_slots[i:i+file_size] == ([-1] * file_size):
                return range(i, i + file_size)

        return None

    def compact(self):
        disk_slot_copy = self.disk_slots.copy()
        for file_id in range(self.max_id, -1, -1):
            print(file_id)
            block = self.find_file_block(file_id)
            size = len(block)
            free_space = self.find_free_space(disk_slot_copy, size)
            if free_space is not None and free_space[0] < block[0]:
                for i in free_space:
                    disk_slot_copy[i] = file_id
                for i in block:
                    disk_slot_copy[i] = -1

        return disk_slot_copy