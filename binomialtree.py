import numpy as np


def print_tree(tree, title=""):
    print("\n" + title + "\n")
    n = len(tree)

    for i, level in enumerate(tree):
        spaces = " " * (4 * (n - i))
        values = "      ".join(f"{x:.2f}" for x in level)
        print(spaces + values)


def binomial_tree_option(
    S, K, T, r, sigma, N, option_type="call"
):

    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u

    a = np.exp(r * dt)
    p = (a - d) / (u - d)
    q = 1 - p

#Arbre du sous-jacent


    stock_tree = []

    for i in range(N + 1):
        level = []
        for j in range(i + 1):
            price = S * (u ** j) * (d ** (i - j))
            level.append(price)
        stock_tree.append(level)


    #  Payoff maturité


    option_tree = []
    last_level = []

    for price in stock_tree[-1]:
        if option_type == "call":
            last_level.append(max(price - K, 0))
        else:
            last_level.append(max(K - price, 0))

    option_tree.append(last_level)


    #  Backward induction


    for i in range(N - 1, -1, -1):
        level = []
        for j in range(i + 1):
            value = np.exp(-r * dt) * (
                p * option_tree[0][j + 1] +
                q * option_tree[0][j]
            )
            level.append(value)

        option_tree.insert(0, level)


    print("u=",u)
    print("d=",d)
    print("a=",a)
    print("p=",p)
    print_tree(stock_tree, "🌳 ARBRE DES PRIX DU SOUS-JACENT")
    print_tree(option_tree, "💰 ARBRE DES VALEURS DE L'OPTION")

    print("\n🎯 Prix de l'option =", round(option_tree[0][0], 4))

    return option_tree[0][0]


# Exemple
binomial_tree_option(
    S=100,
    K=100,
    T=1,
    r=0.05,
    sigma=0.20,
    N=3,
    option_type="call"
)
