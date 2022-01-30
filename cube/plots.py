import matplotlib.pyplot as plt
import pandas as pd

# df = pd.read_csv("analytical_T.txt", names=["T"], sep=" ")
# df.plot()
# plt.show()


results = pd.read_csv(
    "stardis_result_N10000.txt", index_col="#time", delim_whitespace=True
)

results["Temperature"].plot()
plt.show()
