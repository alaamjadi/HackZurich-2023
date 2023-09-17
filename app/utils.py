import pickle


def save_dict_as_pickle(labels, filename):
    with open(filename, "w+b") as handle:
        pickle.dump(labels, handle, protocol=pickle.HIGHEST_PROTOCOL)
    handle.close()

    # import pandas as pd
    # with open(filename, "rb") as f:
    #     object = pickle.load(f)
    # df = pd.DataFrame([object])
    # df = df.transpose()
    # df.to_csv('../results/prettyResults.csv')


