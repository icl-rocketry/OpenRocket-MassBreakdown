# A quick function to capture the masses of each component in an OpenRocket .rkt model
# and to produce a mass breakdown

from prettytable import PrettyTable as pt
import csv


def massBreakdown(path, boosters, propellant):
    components = ["Boosters", "Propellant"]
    masses = [boosters, propellant]
    raw = []

    with open(path, 'r') as f:  # (Sporadic_Impulse1.rkt)

        for i in range(0, 2000, 2):
            data = f.readline()
            if data == '':
                break
            raw.append(data.lstrip())

        for j in range(5, len(raw)):  # 5 is to prevent 'rocket' appearing as a component
            if raw[j].startswith('<KnownMass>'):
                masses.append(float(raw[j][11:-13])/1000)
            if raw[j].startswith('<Name>'):
                components.append(raw[j][6:-8])

    x = pt()
    x.field_names = ["Components", "Masses"]

    with open("massBreakdown.csv", "w+") as out:

        out_writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        out_writer.writerow(['Component', 'Mass'])

        for i in range(0, len(masses)):
            x.add_row([components[i], masses[i]])
            out_writer.writerow([components[i], masses[i]])

    print(x)


# Call

path = input("Enter file path for .rkt model: ")
b = float(input("Enter booster mass (kg): "))
p = float(input("Enter the propellant mass (kg): "))  # Model the dry engine mass in an inner tube

massBreakdown(path, b, p)
