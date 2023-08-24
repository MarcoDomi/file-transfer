from tqdm import tqdm, trange
from time import sleep

pbar = tqdm(total=100)
for i in range(10):
    sleep(0.25)
    if i == 5:
        pbar.reset()
    pbar.update(12)
    #pbar.set_description("Processing %s" % char)
pbar.close()