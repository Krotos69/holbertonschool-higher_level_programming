#!/usr/bin/pyhton3
"""Task 03 - Counted Iterator"""
class CountedIterator:
	"""An iterator that counts how many items have been iterated over."""

	def __init__(self, iterable):
		self._iterable = iterable
		self._index = 0
		self._count = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self._index >= len(self._iterable):
			raise StopIteration
		item = self._iterable[self._index]
		self._index += 1
		self._count += 1
		return item

	def get_count(self):
		"""Return the number of items iterated over."""
		return self._count