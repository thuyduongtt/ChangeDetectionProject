import matplotlib

#if not('DISPLAY' in os.environ):
matplotlib.use("Agg")

import seaborn as sns
sns.set()
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

from datetime import *

months = ["unk","jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
month = (months[datetime.now().month])
day = str(datetime.now().day)

