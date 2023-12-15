import matplotlib.pyplot as plt

def create_bar_chart():
    pojazdy=['car','public_transport','bike','on_foot']
    ile=[25,19,32,7]
    plt.bar(pojazdy,ile,color=['blue','orange','green','red'])

    plt.title("metody przyjazdu do pracy")
    plt.ylabel("ilość osób")
    plt.xlabel("środek transportu")

    plt.show()

create_bar_chart()