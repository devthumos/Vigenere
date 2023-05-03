import re
import pandas as pd

def batches(mensagem_cifrada, key_size):
    batch_list = []
    for i in range(key_size):
        aux_group = []
        for k in range(i, len(mensagem_cifrada), key_size):
            aux_group.append(mensagem_cifrada[k])

        batch_list.append(aux_group)

    return batch_list

def distribution(mensagem_cifrada):
    dist = {x: [0] for x in "abcdefghijklmnopqrstuvwxyz"}
    for i in mensagem_cifrada:
        dist[i][0] += 1

    tam = len(mensagem_cifrada)
    for i in dist:
        dist[i][0] = dist[i][0]/tam

    return dist

def write_csv(df_final, key_size):
    df_final.to_csv(r"Distributions/distribution.csv", sep=",", header=True, index=False, decimal=".")

def pbi_distributions(mensagem_cifrada, key_size):
    mensagem_cifrada_tratada = re.sub(r"[^a-z]", r"", mensagem_cifrada)

    groups = batches(mensagem_cifrada_tratada, key_size)

    dis_list = [distribution("".join(group)) for group in groups]

    dis_df_list = [pd.DataFrame(dis).T for dis in dis_list]
    for k, df in enumerate(dis_df_list):
        df.columns = ["rf"]
        df["letter"] = df.index
        df["distribution"] = k+1
    df_final = pd.concat(dis_df_list)

    write_csv(df_final, key_size)
