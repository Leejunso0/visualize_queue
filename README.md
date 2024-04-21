# visualize_queue
this program visualize queue, so you can see and understand how queue makes work
this defaults to to 3 seconds per action. if you want to change time, change plt.pause()

# Example usage

if __name__ == "__main__":

    q1 = QueueVisualization()

    q1.enqueue(12)

    q1.enqueue(3)

    q1.dequeue()

    q1.enqueue(8)

    q1.dequeue()

    plt.show()

