# visualize_queue
this program visualize queue, so you can see and understand how queue makes work
this defaults to to 3 seconds per action. if you want to change time, change plt.pause()

# Example usage
if __name__ == "__main__":
    queue_visualization = QueueVisualization()
    queue_visualization.enqueue(12)
    queue_visualization.enqueue(3)
    queue_visualization.dequeue()
    queue_visualization.enqueue(8)
    queue_visualization.dequeue()
    plt.show()
