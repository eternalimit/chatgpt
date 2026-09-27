class CodeProgramModel:
    def __init__(self):
        self.index_block = -1
        self.blocks = []

    def add_block(self, block):
        self.blocks.append(block)
        self.index_block = len(self.blocks) - 1

    def reset_index(self):
        self.index_block = -1

    def current_block(self):
        if self.index_block == -1:
            return None
        return self.blocks[self.index_block]


# Canonical anchor state
model = CodeProgramModel()
ANCHOR_INDEX_BLOCK = -1

if __name__ == "__main__":
    print(model.index_block)
    print(model.current_block())
