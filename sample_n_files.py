#!/usr/bin/env python

import click
import os
import random
import shutil

@click.command()
@click.option('--count', default=1, help='Number of file to sample.')
@click.option('--prefix', default="", help='Prefix of the files to consider')
@click.option('--printonly', default=False, type=click.BOOL, help='Print only instead of copying')
@click.option('--verbose', default=False, type=click.BOOL, help='Be verbose')
@click.argument('src', nargs=1, type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True))
@click.argument('dst', nargs=1, type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True))
def cli(count, prefix, printonly, verbose, src, dst):
	"""Sample `count` files, copying them from `src` to `dst`"""

	def is_candidate(pathname, prefix=""):
		filename = os.path.basename(pathname)
		if prefix is not None and prefix != "":
			return os.path.isfile(pathname) and filename.startswith(prefix)
		return os.path.isfile(pathname)

	# Based on https://stackoverflow.com/questions/49280966/pulling-random-files-out-of-a-folder-for-sampling
	candidates = [f for f in os.listdir(src) if is_candidate(os.path.join(src, f), prefix)]
	shuffled = list(candidates)
	random.shuffle(shuffled)
	n_to_select = count
	if n_to_select > len(shuffled):
		n_to_select = len(shuffled)
	selected = shuffled[:n_to_select]
	for filename in selected:
		if printonly:
			print(filename)
			# click.echo(filename)
		else:
			if verbose:
				print("Copying... {}".format(filename))
			shutil.copy(os.path.join(src, filename), dst, follow_symlinks=True)


if __name__ == '__main__':
	cli()
