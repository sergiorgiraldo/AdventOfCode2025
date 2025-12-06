import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


class GridVisualizer:
    def __init__(self):
        self.snapshots = []
        self.colors = {
            ".": 0,  # Empty - white
            "@": 1,  # Paper roll - green
            "x": 2,  # Lifted - red
        }
        self.cmap = ListedColormap(["white", "green", "red"])

    def capture(self, grid):
        """Capture current state of the grid"""
        snapshot = [row[:] for row in grid]  # Deep copy
        self.snapshots.append(snapshot)

    def grid_to_array(self, grid):
        """Convert grid to numerical array for plotting"""
        return np.array([[self.colors[cell] for cell in row] for row in grid])

    def show_static(self, figsize=(10, 8)):
        """Display all snapshots in a grid"""
        n = len(self.snapshots)
        cols = min(4, n)
        rows = (n + cols - 1) // cols

        fig, axes = plt.subplots(rows, cols, figsize=figsize)
        if n == 1:
            axes = [axes]
        else:
            axes = axes.flatten() if rows > 1 else [axes]

        for i, snapshot in enumerate(self.snapshots):
            arr = self.grid_to_array(snapshot)
            axes[i].imshow(arr, cmap=self.cmap, vmin=0, vmax=2)
            axes[i].set_title(f"Step {i}")
            axes[i].axis("off")

            # Add grid lines
            for j in range(len(snapshot)):
                for k in range(len(snapshot[0])):
                    axes[i].text(
                        k, j, snapshot[j][k], ha="center", va="center", fontsize=8
                    )

        # Hide unused subplots
        for i in range(n, len(axes)):
            axes[i].axis("off")

        plt.tight_layout()
        plt.show()

    def animate(self, interval=500, figsize=(8, 6)):
        """Create an animation of the grid evolution"""
        fig, ax = plt.subplots(figsize=figsize)

        # Initialize plot objects once
        snapshot = self.snapshots[0]
        arr = self.grid_to_array(snapshot)
        im = ax.imshow(arr, cmap=self.cmap, vmin=0, vmax=2)
        title = ax.set_title(f"Step 0 - Lifted rolls shown in red")
        ax.axis("off")

        # Create text objects once
        texts = []
        for i in range(len(snapshot)):
            row_texts = []
            for j in range(len(snapshot[0])):
                t = ax.text(
                    j,
                    i,
                    snapshot[i][j],
                    ha="center",
                    va="center",
                    fontsize=10,
                    color="black" if snapshot[i][j] != "x" else "white",
                )
                row_texts.append(t)
            texts.append(row_texts)

        def update(frame):
            # Update image data
            snapshot = self.snapshots[frame]
            arr = self.grid_to_array(snapshot)
            im.set_array(arr)
            title.set_text(f"Step {frame} - Lifted rolls shown in red")

            # Update text
            for i in range(len(snapshot)):
                for j in range(len(snapshot[0])):
                    texts[i][j].set_text(snapshot[i][j])
                    texts[i][j].set_color("black" if snapshot[i][j] != "x" else "white")

            return [im, title] + [t for row in texts for t in row]

        anim = animation.FuncAnimation(
            fig,
            update,
            frames=len(self.snapshots),
            interval=interval,
            repeat=True,
            blit=True,
        )
        plt.show()
        return anim
