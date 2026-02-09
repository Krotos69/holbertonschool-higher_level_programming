#!/usr/bin/python3
"""Task 02 - Verbose List"""

class VerboseList(list):
    """A list that prints a message every time an item is added."""

    def append(self, item):
        super().append(item)
        print(f"Adding {item} to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extending the list with {len(items)} items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removing {item} from the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popping {item} from the list.")
        return item
