# collect run time usage. generates a table/ graphs for the results.

import timeit
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from naiveTextSearch import naiveSearch
from boyerMoore import boyerMooreSearch


def readText():
    textContent = ""
    with open('henrickIbsen.txt', 'r') as file:
        textContent = file.read()
    return textContent

# generate ran information after timing runtime of algorithm using text
def takeMetrics(searchFunc, text):
    textSizes = [1_000, 5_000, 10_000, 15_000, 50_000, 100_000, 200_000, len(text)]
    runtimes = []
    for chunkSize in textSizes:
        textChunk = text[:chunkSize]
        pattern = textChunk[(chunkSize - 50):]

        # Measure runtime using timeit
        num_runs = 10000
        runtime = timeit.timeit(lambda: searchFunc(pattern, textChunk), number=num_runs)
        runtimes.append(runtime)
    return zip(textSizes, runtimes)


def plot_data(data,x):
    """Create a table and plot a graph from the given data."""
    # Create a PrettyTable
    table = PrettyTable()
    table.field_names = ["Input Size", "Running Time (s)"]

    size, runtime = [], []
    # Populate the table with data
    for input_size, running_time in data:
        table.add_row([input_size, running_time])
        size.append(input_size)
        runtime.append(running_time)
    
    table.title=x
    print(table)  # Print the table
    

    """Plot algorithm running time vs. input size as a line graph."""
    plt.title(x)
    plt.plot(runtime, size, 'o-')
    plt.ylabel('Input Size')
    plt.xlabel('Running Time (s)')
    plt.title(f'Running Time vs. Input Size for {x}')
    plt.show()

def main():
    text = readText()
    metrics1 = takeMetrics(naiveSearch, text)
    metrics2 = takeMetrics(boyerMooreSearch, text)
    # plot_data(metrics1,"naive search")
    plot_data(metrics2,"boyer moore")

if __name__ == "__main__":
    main()
